# EJERCICIO SEMANA 1: Ciclo Build-Measure-Learn

## Enunciado

Diseña e implementa un ciclo completo Build-Measure-Learn para validar una hipótesis crítica de una idea de negocio. Tu objetivo es iterar en **máximo 2 ciclos**, cada uno completado en 3-5 días, para aprender si tu supuesto fundamental es válido o requiere un pivot.

**Contexto**: Este ejercicio simula la realidad de startup. No puedes pasar meses perfeccionando un producto sin validar si alguien lo quiere. Debes construir lo mínimo viable, sacarlo al mercado (aunque sea de forma limitada), medir qué sucede, y decidir qué hacer con esa información.

## Instrucciones Paso a Paso

### Paso 1: Define Tu Idea y Hipótesis Principal (Día 1)
- Elige una idea de negocio simple (no necesita ser revolucionaria; puede ser un servicio, app, o producto físico básico).
- Escribe en una oración: *"Si [target customer] tuviera [problema], pagaría por [mi solución]"*.
- Identifica cuál es el supuesto MÁS riesgoso. Ese será tu hipótesis a validar en este ciclo.
- **Ejemplo**: "Si estudiantes de ingeniería tuvieran dificultad organizando sus proyectos, pagarían por una plataforma de colaboración simple."

### Paso 2: Diseña Tu MVP (Día 1-2)
- Define qué features MÍNIMAS necesitas para validar tu hipótesis (no perfeccionismo).
- Describe tu MVP en máx. 5 líneas: qué hace, para quién, y cómo lo entregarás.
- Estima: tiempo de construcción, costo, y número de usuarios que necesitas para aprender algo significativo (min. 10-20).
- **Constraint**: Tu MVP debe estar listo en 3-5 días. Si no cabe, simplifica más.

### Paso 3: Build - Implementa Tu MVP (Día 2-4)
- Construye tu MVP dentro de tu timeframe.
- Documental qué decidiste INCLUIR y qué EXCLUISTE, y por qué.
- Toma capturas de pantalla o fotos si es relevante.
- **Nota**: Si usas herramientas no-code (Webflow, Airtable, etc.), está totalmente bien.

### Paso 4: Measure - Lanza y Recopila Datos (Día 4-5)
- Presenta tu MVP a mínimo 10-15 potenciales clientes (pueden ser amigos, compañeros, contactos relevantes).
- Para cada persona, registra:
  - ¿Entienden qué es el producto? (sí/no)
  - ¿Ven un problema que resuelve? (sí/no)
  - ¿Pagarían por esto? (sí/no/talvez cuánto)
  - 1-2 comentarios clave (qué les gustó, qué no)
- Calcula: % de validación (ej: 6 de 12 dijeron "sí pagaría" = 50%).

### Paso 5: Learn - Analiza Resultados (Día 5)
- Resume en 1 página: ¿Qué salió como esperabas? ¿Qué sorprendió?
- Responde: **¿Tu hipótesis se validó (≥70%), es débil (40-70%), o fue refutada (<40%)?**
- Identifica 2-3 ajustes basados en feedback concreto.

### Paso 6: Decide - Pivot o Persevere (Día 5)
- Si validación ≥70%: PERSEVERA. Define próximas 3 features a agregar y por qué.
- Si 40-70%: PIENSA. ¿Cambias algo del MVP o cambias el mercado? Propón 1 ajuste.
- Si <40%: CONSIDERA PIVOTS. ¿Hay un problema alternativo que viste? ¿Otro mercado? Describe 1 pivot viable.

### Paso 7: Itera (Opcional, Día 6-7)
- Si tienes tiempo, implementa el ajuste o pivot y repite pasos 4-6 en un segundo ciclo.
- Compara resultados: ¿aprendiste algo diferente?

### Paso 8: Documenta Todo (Día 7)
- Entrega un reporte (2-4 páginas) con: hipótesis, MVP descrito, datos de validación, análisis, y decisión.

## Ejemplo / Caso de Referencia

**Idea**: App para reservas de cancha de fútbol 5

**Hipótesis**: "Jugadores de fútbol gastarían $5-10 USD por evitar gestionar reservas por WhatsApp."

**MVP**: Landing page básica + formulario de pre-registro + muestra de 3 canchas locales con horarios (datos pegados a mano, sin base de datos).

**Lancé a**: 12 amigos + 8 contactos en grupos de fútbol.

**Resultados**: 
- 8/20 dijeron "sí pagaría" (40%)
- Feedback: "Está bien, pero quiero ver opiniones de otras personas sobre las canchas"
- Sorpresa: 5 personas preguntaron por sistema de reputación, algo que no había considerado.

**Decisión**: Débil validación. Pivoté: agregar reviews de canchas (hipótesis: el valor real es confianza, no solo reserva). Segundo ciclo: 12/15 dijeron sí (80%).

## Rúbrica de Evaluación

| Criterio | 0-2 pts | 3-5 pts | 6-8 pts | 9-10 pts |
|----------|---------|---------|---------|----------|
| **Claridad de Hipótesis** | No hay hipótesis clara o es demasiado vaga | Hipótesis definida pero con supuestos múltiples | Hipótesis clara pero podría ser más específica | Hipótesis explícita, verificable, y con un supuesto central claro |
| **MVP Realmente Mínimo** | No es viable en el timeframe; demasiado ambicioso | MVP construido pero con features innecesarias | MVP funcional pero con 1-2 features borderline | MVP perfecto: exactamente lo necesario para validar la hipótesis |
| **Medición Rigurosa** | Datos cualitativos sin estructura; <5 usuarios | Datos semi-estructurados; 5-10 usuarios | Datos bien estructurados; 10-15 usuarios; algunos sesgos | Datos claros, método reproducible; 15+ usuarios; análisis sin sesgo |
| **Decisión Fundamentada** | Decisión arbitraria o sin base en datos | Decisión con base en datos pero análisis superficial | Decisión con análisis claro; considera alternativas | Decisión explícita (perseverar/pivotar) basada en evidencia; plan siguiente claro |

**Puntaje Total**: Suma los 4 criterios. Máx. 40 pts, se convierte a escala 0-10.

## Solución Esperada

Una buena solución incluye:

1. **Hipótesis verificable**: "Si [customer específico] tuviera [problema específico], lo resolvería [solución específica]" — con UN supuesto central.

2. **MVP entregado en plazo**: Funciona, lo hiciste en 3-5 días, y está documentado con capturas/fotos.

3. **Datos claros de validación**: Mínimo 10-15 usuarios consultados, registrados de forma consistente (tabla con sí/no/tal vez + comentario).

4. **Análisis honesto**: No sobre-interpretes. Si 40% validó, di "débil" aunque te agrade la idea. Cita feedback específico, no general.

5. **Decisión explícita**: Escribe la palabra "PERSEVERAR" o "PIVOTAR", explica por qué, y describe los próximos 3 pasos (features a agregar, mercado a probar, o problema alternativo a validar).

El objetivo es que practiques el ciclo Lean Startup con urgencia real: tiempo limitado, presupuesto limitado, y decisiones basadas en datos, no en intuición.
