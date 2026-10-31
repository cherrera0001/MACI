"""Memoria episódica en caliente y búsqueda asociativa (H-10.3, T-10.1.1, T-10.1.2).

Todo corre sin LLM y sin red: los recuerdos se registran con registrar_recuerdo
y la verdad la garantiza evidencia.validar sobre fids reales del índice.
"""
from datito import evidencia
from datito.indice import Indice


def _indice_semilla():
    ind = Indice()
    fids = [
        ind.registrar_recuerdo(
            "Rufo es el perro de la persona; vive con ella desde cachorro "
            "y le hace compania en las mananas.", "semilla:rufo"),
        ind.registrar_recuerdo(
            "La hermana de la persona se llama Carmen y vive en Temuco; "
            "se ven juntas cada vacaciones de verano.", "semilla:carmen"),
        ind.registrar_recuerdo(
            "El veterinario del Dr. Fuentes atiende a Rufo cuando esta "
            "enfermo; queda cerca de la plaza.", "semilla:veterinario"),
        ind.registrar_recuerdo(
            "A la persona le gusta tejer bufandas para sus nietas en las "
            "tardes de invierno.", "semilla:tejido"),
        ind.registrar_recuerdo(
            "Carmen recomendo el telefono nuevo que la persona usa ahora; "
            "lo compraron juntas en el centro.", "semilla:telefono"),
        ind.registrar_recuerdo(
            "La persona guarda las fotos de sus nietas en el telefono "
            "nuevo para ensenarselas cuando la visitan.", "semilla:fotos"),
    ]
    return ind, fids


def test_registro_caliente_ids_correlativos():
    ind, fids = _indice_semilla()
    assert fids == [f"memoria#{i}" for i in range(1, 7)]
    assert all(fid in ind.textos for fid in fids)
    assert ind.referencias["memoria#1"] == ("memoria", "semilla:rufo")


def test_persistencia_recarga_y_citabilidad(tmp_path):
    ind, fids = _indice_semilla()
    ind.guardar(tmp_path / ".indice")
    ind2 = Indice.cargar(tmp_path / ".indice")
    for fid in fids:
        assert fid in ind2.textos
    # un recuerdo recargado es citable y valida con el gate intacto
    val = evidencia.validar(
        f"Recuerdo que {ind2.textos['memoria#1'][:50]} [memoria#1]", ind2)
    assert val.ok and val.citas == ["memoria#1"]


def test_buscar_plano_no_conecta_recuerdos():
    ind, _ = _indice_semilla()
    plano = ind.buscar("como esta mi perro", k=4)
    fids_planos = [f for f, _ in plano]
    assert "memoria#1" in fids_planos
    assert "memoria#3" not in fids_planos   # el veterinario no comparte términos de la consulta


def test_buscar_asociativo_un_salto_por_puente():
    ind, _ = _indice_semilla()
    res = ind.buscar_asociativo("como esta mi perro", k=4, saltos=1)
    fids = [f for f, _, _ in res]
    assert "memoria#3" in fids
    traza = next(t for f, _, t in res if f == "memoria#3")
    assert "rufo" in traza                  # el puente fue la entidad compartida
    assert all(f in ind.textos for f in fids)   # la asociatividad no inventa fids


def test_buscar_asociativo_multisalto():
    ind, _ = _indice_semilla()
    plano = ind.buscar("mi hermana", k=4)
    assert "memoria#6" not in [f for f, _ in plano]
    un_salto = [f for f, _, _ in ind.buscar_asociativo("mi hermana", k=6, saltos=1)]
    assert "memoria#2" in un_salto and "memoria#5" in un_salto
    assert "memoria#6" not in un_salto      # a un salto no llega: puente telefono esta en #5
    dos_saltos = [f for f, _, _ in ind.buscar_asociativo("mi hermana", k=6, saltos=2)]
    assert "memoria#6" in dos_saltos        # 2° salto: #2 --carmen--> #5 --telefono--> #6
