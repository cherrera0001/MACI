# FCD-2026-2_08_DL_LLMs_Agents

> Material de clase de Fundamentos de Ciencia de Datos, UdeC T2-2026.
> Texto extraido de `FCD-2026-2_08_DL_LLMs_Agents.pdf` para busqueda e indexacion.
> 66 laminas. Las figuras no se extraen: si una lamina
> depende de un grafico, hay que abrir el PDF.

---

## Lamina 1

Fundamentos en Ciencia de 
Datos
Últimos Avances en 
Inteligencia Artiﬁcial
Guillermo Cabrera-Vives
Ingeniero Civil Informático
MSc en Ciencias de la Computación, 
Universidad de Chile.
Ph.D. en Ciencias de la Computación, 
Universidad de Chile.
guillecabrera@inf.udec.cl
CLASE #8

## Lamina 2

Aprendizaje Supervisado
• Utiliza un conjunto de entrenamiento compuesto por:
○ atributos xi
○ etiquetas yi
• Objetivo: determinar una función que tome los atributos y 
prediga la etiqueta
Positivos
Negativos
• Si la etiqueta a predecir es un valor real, entonces lo 
llamamos regresión.
• Si la etiqueta a predecir es una categoría, entonces lo 
llamamos clasiﬁcación.
MÓDULOS
MÓDULOS

## Lamina 3

AGENDA
UNIDAD TEMA
01 Deep Learning
02 I.A. Generativa: Large Language Models (LLMs) y difusión
03 Agentes
04 Últimos avances
Clase 8

## Lamina 4

• Area que trabaja en sistemas que 
puedan:
• Razonar: procesar datos y crear 
nuevo conocimiento a partir del 
existente
• Actuar: tomar decisiones y modiﬁcar 
el medio ambiente
Inteligencia Artiﬁcial

## Lamina 5

• La Inteligencia Artiﬁcial es la 
nueva electricidad
• La electricidad cambió 
signiﬁcativamente la 
industria.
• Transporte, manufactura, 
salud, comunicaciones, etc.
• La IA esta haciendo lo mismo 
hoy día.
Inteligencia Artiﬁcial
Andrew Ng

## Lamina 6

• 1.2M images de entrenamiento
• 1000 categorías de objetos
IMAGENET 
Large Scale Visual Recognition Challenge

## Lamina 7

https://developer .nvidia.com/deep-learning
IMAGENET 
Large Scale Visual Recognition Challenge

## Lamina 8

Técnicas de ML en función de la 
cantidad de datos
Desempeño
Cantidad de Datos
Deep Learning
Algoritmos Clásicos

## Lamina 9

Interés en Deep Learning

## Lamina 10

• Conjunto de algoritmos que modelan los datos a través de múltiples 
niveles de abstracción usando un conjunto de capas jerárquicas
Deep Learning

## Lamina 11

Deep Learning

## Lamina 12

Deep Learning vs Machine 
Learning Clásico
https://www.xenonstack.com/blog/log-analytics-deep-machine-learni
ng/

## Lamina 13

Unidad base: el perceptrón

## Lamina 14

Ejemplo: regresión

## Lamina 15

Ejemplo: regresión
Σ1

## Lamina 16

Función de Costo

## Lamina 17

Función de Costo

## Lamina 18

Minimización de Funciones de 
Costo
Σ1

## Lamina 19

Descenso de Gradiente 
tasa de aprendizaje

## Lamina 20

Redes Neuronales
Σ
1

## Lamina 21

Σ
1
Redes Neuronales

## Lamina 22

Redes Neuronales

## Lamina 23

Redes Neuronales

## Lamina 24

Redes Neuronales

## Lamina 25

Redes Neuronales

## Lamina 26

PERRO
FORWARD
Redes Neuronales

## Lamina 27

GATO
Redes Neuronales

## Lamina 28

GATO
Redes Neuronales

## Lamina 29

GATO
Redes Neuronales

## Lamina 30

GATO
Redes Neuronales

## Lamina 31

GATO
BACKWARD
Redes Neuronales

## Lamina 32

https://peltarion.com/blog/data-science/self-attention-video

## Lamina 33

General Language Understanding Evaluation (GLUE)
• Un punto de referencia de nueve tareas de comprensión del lenguaje, basadas en oraciones 
o pares de oraciones, basado en conjuntos de datos existentes y seleccionados para cubrir 
una amplia gama de tamaños de conjuntos de datos, géneros textuales y grados de 
diﬁcultad.
• Un conjunto de datos de diagnóstico diseñado para evaluar y analizar el rendimiento del 
modelo con respecto a una amplia gama de fenómenos lingüísticos presentes en el lenguaje 
natural.
• Una tabla de clasiﬁcación pública para el seguimiento del rendimiento en el punto de 
referencia y un panel para visualizar el rendimiento de los modelos en el conjunto de 
diagnóstico.
Natural Language Processing
https://gluebenchmark.com/

## Lamina 34

Transformers in NLP
 GLUE
Pre-OpenAI SOTA 74%
OpenAI GPT (2017) 75.1%
BERT (2018) 82.1%
RoBertA (2019) 88.5%
XLNet (2019) 88.4%
ALBERT (2019) 89.4%
ELECTRA (2020) 85.1%
https://medium.com/deepset-ai/going-beyond-squad-part-1-question-answering-in-different-languages-8eac6cf56f21

## Lamina 35

Self-attention
El perro café pusose y ladróme
feliz
0.0 0.3 0.1 0.0 0.0 0.3 0.0 0.0 0.3
Desde grandes modelos de lenguaje a la I.A. general guillecabrera@inf.udec.cl

## Lamina 36

Foundation Models
Los modelos Fundacionales (BERT, GPT-3, 
CLIP, Codex) son modelos entrenados con 
muchos datos de modo que puedan adaptarse 
a una amplia gama de tareas posteriores.
https://hai.stanford.edu/news/introducing-center-research-foundation-models-crfm
Desde grandes modelos de lenguaje a la I.A. general guillecabrera@inf.udec.cl
Devlin et.al., BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding, 2019, NAACL-HLT

## Lamina 37

The
brown
dog
happy
became
barked
me
at
and
Transformer Encoder
BERT

## Lamina 38

The
MASK
dog
happy
became
MASK
me
at
and
Transformer Encoder
BERT
brown
barked
Predicción
(softmax)
Masked 
Language 
Model 
(MLM)
BERT enmascara un 
15% de los tokens 
de cada secuencia 
al azar.

## Lamina 39

The
brown
dog
happy
became
barked
me
at
and
Transformer Encoder
Auto-Regressive Generative 
Transformers

## Lamina 40

The
brown
dog
happy
became
barked
at
and
Transformer Encoder
Auto-Regressive Generative 
Transformers
MASKme

## Lamina 42

Dos procesos
• Proceso de difusión hacia adelante: añade ruido gradualmente a la entrada.
• Proceso de eliminación de ruido inverso: aprende a generar datos mediante 
la eliminación de ruido.
Denoising Diffusion-based Generative Modeling: Foundations and Applications, CVPR 2022 Tutorial
Denoising Diffusion Models

## Lamina 43

Latent Space Diffusion

## Lamina 45

LLMs:
● Tienen billones de parámetros que ajustar!
○ GPT-3 tiene 175B de parámetros
○ Llama-2 tiene versiones de 7B, 13B, 70B
● Esto quiere decir que necesitan muchos datos y poder de cómputo para entrenarse
● Son muy buenos como:
○ Asistente de escritura
○ Asistente de codeo
● Son muy malos para:
○ Obtener respuestas basadas en hechos (alucinan)
○ Usar información posterior a su entrenamiento
○ Razonar y planificar
● Simplemente imitan a sus conjuntos de entrenamiento
Agentes

## Lamina 46

Agentes
● Un agente puede realizar acciones autónomas sin intervención humana constante.
● Puede contar con un humano en el proceso para mantener el control.
● Los agentes tienen memoria para almacenar preferencias individuales y permitir la 
personalización. También puede almacenar conocimiento. 
● Un LLM puede encargarse del procesamiento de información y la toma de 
decisiones.
● Los agentes deben ser capaces de percibir y procesar la información disponible 
en su entorno.
● Los agentes también pueden usar herramientas como acceder a internet, usar 
intérpretes de código y realizar llamadas API.
● Los agentes también pueden colaborar con otros agentes o con humanos.

## Lamina 47

Agentes
https://k21academy.com/agentic-ai/what-is-agentic-ai/

## Lamina 48

Agentes
https://k21academy.com/agentic-ai/what-is-agentic-ai/
Ejemplos:
• Agentes de monitoreo y mantenimiento: supervisan sensores, cámaras y maquinaria para 
detectar anomalías, riesgos y fallas en tiempo real.
• Agentes operacionales: coordinan producción, logística, inventario y procesos industriales 
utilizando datos y sistemas empresariales.
• Agentes de análisis documental y reportes: generan y resumen informes técnicos, médicos 
(por ejemplo radiológicos), operacionales y de mantenimiento.
• Agentes de asistencia y soporte inteligente: ayudan a operadores y equipos técnicos 
consultando manuales, diagnosticando problemas y recomendando acciones.

## Lamina 49

2. La revolución de Deep 
Learning

## Lamina 50

Interés en Deep Learning

## Lamina 51

2018 Turing Award
Recipients of the 2018 ACM A.M. Turing Award for conceptual and 
engineering breakthroughs that have made deep neural networks a critical 
component of computing.
Desde grandes modelos de lenguaje a la I.A. general guillecabrera@inf.udec.cl

## Lamina 52

https://futureoflife.org/open-letter/pause-giant-ai-experiments/
“It is because there is an unexpected acceleration –I probably 
would not have signed such a letter a year ago– that we need to 
take a step back, and that my opinion on these topics has 
changed.”
“We must continue to fight for the well-being of humanity and for the 
development of beneficial AI applications, such as those to address 
the climate crisis. This will require changes at the level of each 
country and the adoption of international treaties. We succeeded in 
regulating nuclear weapons on a global scale after World War II, we 
can reach a similar agreement for AI.”
https://yoshuabengio.org/2023/04/05/slowing-down-development-of-ai-systems-passing-the-turing-test/

## Lamina 53

https://www.semianalysis.com/p/google-we-have-no-moat-and-neither
But the uncomfortable truth is, we aren’t positioned to win this arms race and neither is OpenAI. While we’ve been squabbling, a third 
faction has been quietly eating our lunch.
I’m talking, of course, about open source. Plainly put, they are lapping us.
The Timeline
Feb 24, 2023 - LLaMA is Launched (Meta)
March 3, 2023 - The Inevitable Happens: LLaMA leaked
March 12, 2023 - Language models on a Raspberry Pi
March 13, 2023 - Alpaca: Fine Tuning on a Laptop
March 18, 2023 - Now It’s Fast: LLaMA runs on a MacBook CPU
March 19, 2023 - A 13B model achieves “parity” with Bard
March 25, 2023 - Choose Your Own Model
March 28, 2023 - Celebras: Open Source GPT-3
March 28, 2023 - Multimodal Training in One Hour
April 3, 2023 - Real Humans Can’t Tell the Difference Between a 13B Open Model and ChatGPT
April 15, 2023 - Open Source RLHF at ChatGPT Levels

## Lamina 54

Desde grandes modelos de lenguaje a la I.A. general guillecabrera@inf.udec.cl

## Lamina 56

3. El impacto de la IA en la 
industria

## Lamina 57

Adopción de IA

## Lamina 58

● La inversión en inteligencia artiﬁcial ha 
crecido de forma explosiva en la última 
década. 
● La IA pasó de ser una tecnología 
emergente a una prioridad estratégica 
para empresas e industrias. 
● En 2025, la inversión en IA alcanzó los 
581,7 mil millones USD, principalmente 
por inversión privada, fusiones y 
adquisiciones.
● 
Inversión en IA

## Lamina 59

● El uso de IA en empresas sigue 
creciendo rápidamente. 
● Sin embargo, la mayoría de las 
organizaciones aún se 
encuentra en etapas de 
experimentación o pilotos. 
● Solo cerca de un tercio ha 
comenzado a escalar sus 
soluciones de IA.
● 
Uso de IA en la industria

## Lamina 60

● Aunque todavía son pocos los 
casos donde la IA impacta 
directamente los resultados 
ﬁnancieros de toda la 
empresa, muchas 
organizaciones ya reportan 
reducción de costos en casos 
de uso especíﬁcos. 
● Los mayores beneﬁcios se 
observan en ingeniería de 
software, manufactura y 
tecnologías de la información.
Uso de IA en la industria

## Lamina 61

● Los mayores 
aumentos de 
ingresos asociados 
al uso de IA se 
observan en 
marketing, ventas 
y desarrollo de 
productos y 
servicios.
Uso de IA en la industria

## Lamina 62

El mercado laboral

## Lamina 64

…las cosas están cambiando

## Lamina 65

Comentarios Finales
• La Inteligencia Artiﬁcial está con nosotros.
• El gran boom se debe gracias a las redes neuronales artiﬁciales, la 
gran cantidad de datos que hemos producido como humanidad y a 
avances en cómputo con tarjetas gráﬁcas.
○ Imágenes
○ Texto
○ Videos
• Los agentes pueden razonar y utilizar herramientas para resolver tareas 
cada vez más complejas.

## Lamina 66

Fundamentos en Ciencia de 
Datos
Últimos Avances en 
Inteligencia Artiﬁcial
Guillermo Cabrera-Vives
Ingeniero Civil Informático
MSc en Ciencias de la Computación, 
Universidad de Chile.
Ph.D. en Ciencias de la Computación, 
Universidad de Chile.
guillecabrera@inf.udec.cl
CLASE #8
