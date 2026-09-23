# EJERCICIO SEMANA 5: Levanta una Ronda de Financiamiento

## Enunciado

Prepara y ejecuta una ronda de inversión simulada para tu startup. Tu objetivo es: (1) definir cuánto dinero necesitas y para qué, (2) calcular una valuación defensible, (3) preparar un pitch deck que atraiga inversores, y (4) negociar términos realistas.

**Contexto**: Levantar capital es una habilidad adquirida, no innata. El ejercicio simula el proceso completo: prep, pitch, feedback, negociación. Al final, entenderás qué preguntas hacen los VCs y cómo responder.

## Instrucciones Paso a Paso

### Paso 1: Define Tu Ask (Cuánto y Para Qué) (Día 1)

Responde con precisión:
- **Cuánto dinero necesitas**: Sé específico. Ej: "$350K" no "$algo entre 300K y 500K"
- **Qué hito lograrás con ese dinero en 18 meses**: Ej: "Pasar de 100 a 500 clientes, alcanzar $50K MRR, validar model B2B2C"
- **Presupuesto desglosado**: Dónde va el dinero. Ej:
  - Salarios (2 engineers, 1 sales): $240K
  - Marketing/adquisición: $80K
  - Infraestructura: $20K
  - Overhead: $10K
  - **Total**: $350K

**Validación de realismo**: Divide el ask entre los meses (18). ¿Necesitas $350K / 18 = $19.4K / mes? ¿Eso alcanza para tus hires y operaciones? Si no, ajusta.

### Paso 2: Calcula Valuación (Día 1-2)

**Método 1: Comparable Companies** (mejor para startups con traction)
- Identifica 3-5 startups comparables (mismo sector, etapa similar)
- Busca su última valuación pública o reportada
- Compara métricas: MRR, usuarios, crecimiento

Ejemplo: Otra SaaS en tu sector, levantó seed a $5M post-money con $10K MRR y 500 clientes. Tú tienes $5K MRR y 300 clientes. Tu valuación debería ser ~$2.5M-$3.5M post-money (ajustado por métrica).

**Método 2: Venture Capital Method** (para early stage)
- Asume: ¿Cuánto valor creará tu startup en 5 años? (Ej: $100M empresa)
- ¿Cuántos $ diluyentes esperas levantar? (Ej: $1M total en todas las rondas)
- Divide: $100M / $1M = 100x. Tu ownership hoy con $350K levantar = $350K / $100M = 0.35%
- Valuation post-money = $350K / % investor = $350K / 3.5% ≈ $10M

**Método 3: Heurística (Cuando no hay data)**
- Seed típicamente: $1M-$5M post-money
- Serie A: $7M-$25M post-money
- Ajusta por sector (software escala → valuation alta; hardware escala lenta → baja) y equipo.

**Entrega para Paso 2**:
- Cuál metodología usaste
- Valuación pre-money sugerida
- Valuación post-money después de tu $350K (pre + ask)
- Rango defensible (ej: "$4M-$6M post-money")

### Paso 3: Prepare Pitch Deck (10-15 slides) (Día 2-3)

**Estructura estándar**:

1. **Slide 1: Cover** — Nombre startup, tagline (1 línea), logo, date
2. **Slide 2: Problema** — Qué problema resuelves. Hazlo emocional y cuantificado. Ej: "500K startups LATAM gastan 20 horas/mes en compliance manual. Eso es $5B/año en tiempo perdido."
3. **Slide 3: Solución** — Qué es tu startup. 1 imagen/diagrama + 2-3 líneas. No des vuelta.
4. **Slide 4: Traction (Validación)** — ¿Qué prueba que el problema existe y la solución funciona? Clientes, usuarios, ingresos, NPS, growth rate. Números concretos.
5. **Slide 5: Mercado (TAM/SAM/SOM)** — Tamaño del mercado donde compites.
   - TAM (Total Addressable Market): Mercado global. Ej: "Compliance software LATAM = $5B/año"
   - SAM (Serviceable Available Market): Segment que puedes atacar. Ej: "Startups LATAM con 10-100 empleados = $500M"
   - SOM (Serviceable Obtainable Market): Tu realista en 5 años. Ej: "Nosotros podemos llegar a 10% de SOM = $50M"
6. **Slide 6: Competencia** — Quiénes son. Dónde estás vs. ellos. Por qué ganas.
7. **Slide 7: Modelo de Negocios** — Cómo ganas dinero. Rapidito: "SaaS, $100/empresa/mes, target 500 clientes Year 1."
8. **Slide 8: Team** — Photos, nombres, roles, backgrounds relevantes. "Why you?" Qué los hace capaces de ejecutar.
9. **Slide 9: Financials/Roadmap** — 18-month projection de revenue, clientes, hiring. Visual (gráfico) es mejor que tabla.
10. **Slide 10: Ask** — "Levantamos $350K para [hito]. Esto nos posiciona para [siguiente ronda]."
11. **Slides 11+: Appendix** — Detalles técnicos, customers quotes, financials detallados, legal. Investor pide, tú muestras.

**Tips de diseño**:
- 1 idea principal por slide
- Fuente grande (mínimo 24pt)
- Poco texto; más imágenes/números
- Consistencia visual (colores, fonts)
- Accesibilidad (alto contraste)

### Paso 4: Proyección Financiera (Día 3)

18-month monthly projection:

| Mes | Clientes | MRR | CAC | Churn | Ingresos | Gastos Operacionales | Cash Burn | Runway Meses |
|---|---|---|---|---|---|---|---|---|
| 0 (Hoy) | 100 | $5K | N/A | 5% | $5K | $8K | -$3K | 11.7 |
| 3 | 150 | $7.5K | $2K | 5% | $7.5K | $12K | -$4.5K | 7.8 |
| 6 | 250 | $12.5K | $1.5K | 4% | $12.5K | $15K | -$2.5K | 14 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 18 | 500 | $25K | $1K | 3% | $25K | $20K | +$5K | ∞ |

**Qué mostrar**:
- Crecimiento de clientes (month-on-month)
- Trendline de MRR (debería ser exponencial temprano)
- CAC bajando (economies of scale)
- Churn bajando (product improvements)
- Cuándo llegas a break-even (cash positive)
- Cuánto runway queda en mes 18

**Realismo**: Modera proyecciones. Si hoy tienes $5K MRR y crecimiento 10%/mes, en 18 meses estarías en $25K. Eso es factible. Si proyectas $100K en 18 meses con equipo de 3 personas, es irreal.

### Paso 5: Prepara Respuestas a Preguntas Comunes (Día 3)

VCs típicamente preguntan:

1. **"¿Cuál es tu defensibilidad?"** → Tu moat. ¿Qué te protege cuando competidores clonan?
2. **"¿Por qué este equipo puede hacerlo?"** → Cuáles son tus fortalezas únicas. No digas "trabajamos duro"; di "el CEO vendió SaaS antes y cerró 200K ARR en 3 meses."
3. **"¿Cuál es tu costo de adquisición y lifetime value?"** → Matemáticas de unit economics. Si no las tienes, es red flag.
4. **"¿Cuál es tu mayor riesgo?"** → Sé honesto. No digas "ninguno". Ej: "Dependemos de 1 partner de infraestructura. Si falla, caemos. Plan: redundancia en mes 6."
5. **"¿A cuántas otras startups estás pitcheando?"** → Honestidad. Algunos quieren exclusividad; otros respetan competencia.
6. **"¿Cuál sería una ronda serie A exitosa para ustedes?"** → $X levantados a $Y valuación post-money, logrando $Z MRR.

Prepara 2-3 respuestas sólidas para cada pregunta.

### Paso 6: Pitch (10 minutos) (Día 4)

Practica pitch en voz alta. Cronómetra.
- Primeros 5 minutos: Problema + Solución + Traction
- Siguientes 3 minutos: Team + Mercado + Financials
- Últimos 2 minutos: Ask + Siguiente pasos

**Delivery**:
- Pausa entre slides (3 segundos)
- Mira a la audiencia, no la pantalla
- Entusiasmo genuino; no robótico
- Evita decir "uhh", "eee", "básicamente"

### Paso 7: Negociación Simulada (Día 4-5)

Con un mentor o inversor simulado, practica:
- **Valuación**: "Proponen $3M post-money. Tú quieres $5M. Negocias a $4M."
- **Términos**: "Investor pide liquidation preference participating (toma dinero + ganancias). Tú contrapropon non-participating."
- **Board seat**: "Investor pide asiento en directorio. Tú contrapropon: observador primero, board cuando ronda B."
- **Dilution cap**: "Investor pide sin cap. Tú contrapropon: máx. 10% dilución en futuras rondas."

Documenta qué cediste y qué no. Éste es el aprendizaje real.

### Paso 8: Entrega Final (Día 5)

Entrega:
1. **Pitch deck** (PDF o Google Slides con link)
2. **Documento de Ask** (cuánto, para qué, timeline)
3. **Proyección financiera** (18 meses)
4. **Valoración memo** (cómo la calculaste)
5. **Respuestas a preguntas comunes** (3 párrafos por pregunta)
6. **Debrief de negociación** (qué pasó, qué aprendiste)

## Ejemplo / Caso de Referencia

**Startup: SaaS de Gestión de Inventario para Retail LATAM**

**Ask**: $400K para escalar de 50 a 300 clientes, alcanzar $30K MRR

**Valuación Calculation**:
- Comparable: Otra startup retail tech levantó a $6M post-money con $15K MRR y 150 clientes.
- Nuestra traction: $5K MRR, 50 clientes = 1/3 de comparable
- Sugerida: $6M / 3 = $2M post-money
- Pre-money: $2M - $400K = $1.6M
- Investor recibe: $400K / $2M = 20%

**Pitch Narrative**:
"Retailers LATAM pierden $2B/año en inventory shrink. Nuestro software reduce eso 30%. Tenemos 50 clientes pagando $100/mes. Crecimiento es 40% MoM. Con $400K, llegamos a 300 clientes, $30K MRR, y nos posicionamos para Serie A. Team: Founder 1 vendió 2 exitosas; Founder 2 built software de inventory para BigCo 10 años."

**Financials Projection**:
- Mes 0: $5K MRR, 50 clientes
- Mes 6: $12K MRR, 120 clientes (10% churn, 40% MoM growth)
- Mes 12: $20K MRR, 200 clientes
- Mes 18: $30K MRR, 300 clientes (break-even en mes 15)

**Negociación**:
- Investor propone: $2.5M post-money (25% para ellos)
- Tú contrapropon: $2M post-money (20% para ellos)
- Compromiso: $2.2M post-money (22% para ellos)
- Liquidation: Investor prefiere participating. Tú negocias non-participating (mejor para ti en exit).

## Rúbrica de Evaluación

| Criterio | 0-2 pts | 3-5 pts | 6-8 pts | 9-10 pts |
|----------|---------|---------|---------|----------|
| **Realismo del Ask** | Cantidad vaga o irreal | Cantidad específica pero monto o timeline cuestionable | Cantidad justificada; presupuesto coherente | Ask perfectamente justificado, presupuesto desglosado, timeline realista |
| **Valuación Defensible** | Sin metodología o número random | Metodología débil o valuación inflada | Metodología sólida, 1-2 comparables usados | 3+ metodologías, comparables claros, rangos defensibles |
| **Pitch Deck Calidad** | Incompleto o muy vago | 8-9 slides, pero diseño pobre o mucho texto | 10-12 slides, diseño decente, storytelling claro | 12-15 slides, diseño pulido, narrativa convincente |
| **Financials Creíbles** | Proyecciones heroicas o inconsistentes | Proyecciones moderadas pero sparse (pocos números) | Proyecciones realistas, 18-month detail, varios KPIs | Proyecciones realistas, detalladas, incluye runway y break-even |

**Puntaje Total**: Suma criterios. Max 40 pts → escala 0-10.

## Solución Esperada

Una buena solución:

1. **Ask específico**: "$350K para escalar a 500 clientes en 18 meses" vs. "algo entre 200K y 500K."

2. **Valuación con bases**: Mínimo 2 metodologías (comparables + venture capital method). Valuation pre y post money claras.

3. **Pitch deck profesional**: Diseño limpio, storytelling con arco (problema → pain → solution → traction → team → ask). No más de 15 slides.

4. **Financials honestos**: Crecimiento moderado (20-30% MoM es ambicioso; 50%+ es heroico). Incluye churn realista, CAC, runway.

5. **Preguntas anticipadas**: Respuestas cortas pero sustanciales a 6+ preguntas comunes de VCs.

6. **Negociación informada**: Entiendes que valuación es 1 línea. Términos (liquidation, dilution cap, board) importan igual o más.

El objetivo es que te desensibilices a pitchar, entiendas cómo piensan los inversores, y practiques negociación bajo presión. En el mundo real, esto es lo que determina si tu startup prospera o muere.
