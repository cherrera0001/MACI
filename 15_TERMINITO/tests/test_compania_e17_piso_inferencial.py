"""E-17: piso inferencial importado (ALL #337) y corpus denso (#335).

Cubre D-17.2: bootstrap pareado con IC95 importado de aal.evaluation, 8
sondas de validación congeladas (reportadas, no seleccionadas), rival TF-IDF
de 1 salto sobre el mismo grafo, y la sonda crítica de corpus denso (55
recuerdos con vocabulario compartido). Todo en cursos temporales.
"""
import pytest

from datito import cerebro, eval_conversacion, eval_cerebro, llm

tiene_aal = cerebro.AAL
skip_sin_aal = pytest.mark.skipif(not tiene_aal, reason="aal no instalado")


def test_sondas_congeladas_8_y_separadas_de_la_bateria():
    assert len(eval_cerebro.SONDAS_CONGELADAS) == 8
    assert len(eval_cerebro.SONDAS) == 20
    consultas_bateria = {s.consulta for s in eval_cerebro.SONDAS}
    for s in eval_cerebro.SONDAS_CONGELADAS:
        assert s.consulta not in consultas_bateria, "congelada ≠ batería"


def test_filas_por_sonda_en_forma_agrega():
    ind, fids = eval_cerebro.construir_indice()
    rankings = {s.consulta: eval_cerebro.ranking_baseline(ind, s.consulta)
                for s in eval_cerebro.SONDAS}
    filas = eval_cerebro.filas_por_sonda(rankings, fids, eval_cerebro.SONDAS)
    assert len(filas) == 20
    for fila in filas.values():
        assert set(fila) == {"score_esperada", "aplicada_ok", "rr_leccion"}
        assert 0.0 <= fila["score_esperada"] <= 1.0
        assert isinstance(fila["aplicada_ok"], bool)
        assert fila["rr_leccion"] == 0.0


@skip_sin_aal
def test_piso_inferencial_completo_en_comparar():
    r = eval_cerebro.comparar()
    boot = r["bootstrap"]
    assert boot["n"] == 1000 and boot["seed"] == 42
    assert boot["p2_5"] <= boot["mediana"] <= boot["p97_5"]
    assert isinstance(boot["significativo"], bool)
    # Sondas congeladas reportadas en ambos lados, fuera de la decisión
    assert r["sondas_congeladas"]["n"] == 8
    for lado in ("baseline", "cerebro"):
        assert r["sondas_congeladas"][lado]["validez"] == 1.0
    # Rival TF-IDF (mismo grafo, 1 salto) rankeado sobre las 20 sondas
    assert r["rival_tfidf"]["validez"] == 1.0


@skip_sin_aal
def test_corpus_denso_critico():
    d = eval_cerebro.eval_corpus_denso()
    assert d["recuerdos"] == 55 and d["consultas"] >= 10
    for clave in ("recall_cerebro", "recall_indice", "recall_rival_tfidf"):
        assert 0.0 <= d[clave] <= 1.0
    assert d["colapso"] == (d["recall_cerebro"]
                            < max(d["recall_indice"], d["recall_rival_tfidf"]))
    # Hallazgo #335 local: el índice TF-IDF propio colapsa en corpus denso
    assert d["recall_indice"] == 0.0, \
        "el baseline léxico no sobrevive 55 recuerdos de vocabulario compartido"


@skip_sin_aal
def test_decision_opt_in_por_regla_y_no_por_anomalia():
    r = eval_cerebro.comparar()
    assert r["decision"] == "opt_in", \
        "con la compuerta anti-H4 actual hay regresión P@3: la regla manda opt-in"
    b, c = r["baseline"], r["cerebro"]
    regresion = any(c[m] < b[m] for m in ("mrr", "p3", "rechazo_senuelos"))
    assert regresion, "el motivo del opt-in debe quedar explícito"
    assert r["repeticion"]["rufo_unico"] is True


def test_eval_conversacion_con_llm_mockeado(tmp_path, monkeypatch):
    # D-17.3: con el LLM presente (mockeado), la etapa deja de ser "ausente".
    monkeypatch.setattr(llm, "disponible", lambda: True)
    monkeypatch.setattr(llm, "modelo_instalado", lambda *a, **k: True)
    monkeypatch.setattr(llm, "generar",
                        lambda prompt, **k: "Qué bonito recuerdo. "
                                           "[memoria#1]")
    r = eval_conversacion.correr()
    assert "ollama" not in r["inconcluso_por"], \
        "con LLM presente la etapa no puede quedar inconclusa por ollama"
    assert r["veredicto"] != "" and r["exito_preregistrado"] in (True, False)


def test_eval_conversacion_marca_llm_ausente_honestamente():
    if llm.disponible():
        pytest.skip("hay Ollama real: la inconclusión no aplica")
    r = eval_conversacion.correr()
    assert "ollama" in r["inconcluso_por"]
    assert r["exito_preregistrado"] is False
    assert "INCONCLUSO" in r["veredicto"]
