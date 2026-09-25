# Validación de Fuentes: Cáncer de Mama — Wisconsin (Diagnostic)

## ✅ VALIDADO: Dataset correcto identificado

### Fuentes primarias integradas
- `preinforme_hito1_cancer_mama-v02.pdf` — Análisis exploratorio
- `preinforme_hito2_v02.pdf` — Modelamiento predictivo  
- `Presentacion_Hito2_v2_2.pdf` — Presentación visual

### Dataset verificado: Breast Cancer Wisconsin (Diagnostic)

**Metadatos confirmados**:
- **569 observaciones** ✓ (PDFs coinciden)
- **30 características numéricas** ✓ (10 características × 3 resúmenes: mean, se, worst)
- **357 benignas (62.7%), 212 malignas (37.3%)** ✓ (PDFs coinciden)
- **Autores**: Wolberg, Street, Mangasarian (UCI ML, 1993)
- **DOI**: 10.24432/C5DW2B

**Fuentes verificadas**:
- 🔗 UCI ML Repository: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
- 🔗 Kaggle: https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data

**Paper de referencia**:
- Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). 
  "Nuclear Feature Extraction for Breast Tumor Diagnosis." 
  Proceedings of SPIE, 1905, 861–870. DOI: 10.1117/12.148698

---

## Acciones necesarias

### ANTES de integrar material

1. ✅ **Validar referencia en PDFs**
   - Confirmar autor (Wolberg/Street)
   - Confirmar 569 observaciones
   - Confirmar 30 características
   - Ubicar DOI/URL exacto en UCI

2. ⏳ **Descargar dataset correcto**
   - URL: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+(diagnostic)
   - Guardar en: `F:\MACI\02_DATOS\cancer_wisconsin_diagnostic\`
   - Validar checksum/formato

3. ⏳ **Vincular con clases del profesor (HILT)**
   - ¿Qué láminas mencionan clasificación binaria?
   - ¿Qué láminas mencionan este dataset específico?
   - ¿Hay referencias en Clase 7 (Clasificación)?
   - ¿Hay referencias en certámenes?

4. ⏳ **Actualizar todas las referencias**
   - README.md: precisar DOI/URL
   - INDICE.md: vincular a láminas
   - matriz_confusion_interpretacion_RESUELTO.md: citar clase profesor
   - Todos los visuales: etiquetar [FUENTE · Repo: …] o [FUENTE · Clase HILT: …]

---

## Checklist de coherencia

- [ ] Dataset local coincide con el de PDFs (569, 30 cols)
- [ ] Referencia Wolberg/Street/Mangasarian verificada
- [ ] DOI/URL exacto del UCI documentado
- [ ] Láminas del profesor que cubren este tema identificadas
- [ ] Cada afirmación etiquetada: [FUENTE · Clase X] o [FUENTE · UCI ML]
- [ ] Sin afirmaciones inventadas sin referencia
- [ ] Cifras (39 TP, 72 TN, etc.) trazables a los PDFs
- [ ] Conexión clara: Lámina → Concepto → Caso práctico

---

## Próximos pasos

Pausar integración hasta que:
1. Descargue dataset Wisconsin correcto
2. Verifique coincidencia con PDFs
3. Identifique referencias de HILT
4. Re-etiquete TODO con fuentes
