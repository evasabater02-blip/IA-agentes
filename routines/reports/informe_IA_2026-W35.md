# Informe semanal de Inteligencia Artificial — Semana 35 de 2026 (24-30 de agosto)

## Resumen ejecutivo

La semana ha estado marcada por un giro claro hacia la **trazabilidad y la seguridad** por encima de la pura capacidad computacional. Anthropic ha comenzado a desplegar marcas de agua imperceptibles y señales de procedencia en el contenido generado por Claude para cumplir con las obligaciones de transparencia del artículo 50 del Reglamento de IA de la UE, en vigor desde el 2 de agosto. En paralelo, OpenAI ha pausado partes significativas del entrenamiento de su próximo modelo (nombre en clave "Astra") tras detectar que podría estar alcanzando capacidades cibernéticas "críticas", reforzando sus protocolos de seguridad y monitoreo.

En el plano de los modelos, agosto ha sido un mes especialmente intenso: se han lanzado más de una decena de modelos relevantes (Gemini 3.7 Flash, Grok 4.6, Qwen3.8 Max, GLM-5.2 Turbo, Seedance 2.5, entre otros), con un foco creciente en rendimiento agéntico y eficiencia de inferencia frente al simple escalado de tamaño. A nivel financiero, Anthropic ha reportado un crecimiento explosivo (ingresos anualizados de 65.000 millones de dólares, con 18.000 millones añadidos en solo dos meses) y su primer beneficio operativo, mientras que Nvidia negocia una inversión en Perplexity que valoraría a la startup por encima de los 30.000 millones de dólares.

La tendencia de fondo es doble: por un lado, la IA agéntica sigue consumiendo cada vez más recursos —los agentes ya generan más tráfico de tokens que los humanos según datos de OpenRouter—, obligando a repensar costes e infraestructura; por otro, la presión regulatoria y de confianza está empujando a la industria a competir ya no solo en capacidad, sino en poder demostrar el origen y la veracidad de lo que producen sus modelos.

## Noticias destacadas

**Google lanza Gemini 3.7 Flash**
Google presentó Gemini 3.7 Flash, un modelo optimizado para programación y flujos de trabajo agénticos, construido a partir de mejoras algorítmicas más que de un mayor preentrenamiento. Mientras tanto, Gemini 3.5 Pro, prometido en Google I/O en mayo, sigue sin disponibilidad general tres meses después.
*Fuente: [Router.one](https://router.one/blog/new-llm-models-august-2026), [The AI Insider](https://theaiinsider.tech/2026/08/24/the-week-ahead-in-ai-nvidia-earnings-ai-backlash-alibaba-10b-ai-funding-plus-upcoming-earnings-events/)*

**Anthropic introduce marcas de agua para cumplir con el AI Act de la UE**
Anthropic ha empezado a incorporar marcas de agua invisibles y señales de procedencia en el contenido generado por Claude, en línea con las nuevas exigencias de transparencia de la Unión Europea que entraron en vigor el 2 de agosto de 2026 para chatbots, deepfakes y contenido sintético.
*Fuente: [AI News](https://www.artificialintelligence-news.com/), [IA Regulación](https://iaregulacion.com/ai-act-2-agosto-2026/)*

**OpenAI pausa el entrenamiento de su modelo "Astra" por motivos de seguridad**
OpenAI detuvo una parte significativa del entrenamiento de su próximo modelo tras evaluaciones que sugerían capacidades cibernéticas "críticas", incluyendo posible desarrollo autónomo de exploits de día cero. El modelo pasa a pruebas aisladas con revisión de agencias gubernamentales y organizaciones de seguridad.
*Fuente: [Medium – David Akpovi](https://medium.com/@davidakpovi/ai-news-week-of-august-10-16-2026-af52646d84d2)*

**Anthropic dispara sus ingresos y logra su primer beneficio operativo**
La compañía reportó ingresos anualizados de 65.000 millones de dólares (18.000 millones añadidos en dos meses) y, según otras fuentes, un beneficio operativo de 559 millones de dólares en el segundo trimestre, dos años antes de lo previsto en su propio calendario.
*Fuente: [AI News This Week](https://medium.com/@davidakpovi/ai-news-week-of-august-3-9-2026-8dfa677ffca3)*

**Nvidia negocia entrar en el capital de Perplexity**
Nvidia estaría en conversaciones para invertir en Perplexity a una valoración superior a los 30.000 millones de dólares, mientras la startup supera los 750 millones de dólares de ingresos anualizados.
*Fuente: [The AI Insider](https://theaiinsider.tech/2026/08/24/the-week-ahead-in-ai-nvidia-earnings-ai-backlash-alibaba-10b-ai-funding-plus-upcoming-earnings-events/)*

**Alibaba lanza una ampliación de capital de 10.200 millones de dólares para IA**
Alibaba anunció una colocación de acciones por 80.000 millones de dólares hongkoneses (~10.200 millones de dólares) destinada a financiar chips, infraestructura y desarrollo de modelos de IA.
*Fuente: [The AI Insider](https://theaiinsider.tech/2026/08/24/the-week-ahead-in-ai-nvidia-earnings-ai-backlash-alibaba-10b-ai-funding-plus-upcoming-earnings-events/)*

**Nvidia detalla la arquitectura de su CPU Vera en Hot Chips 2026**
Nvidia reveló los detalles internos de su CPU Vera, con 88 núcleos Olympus propios, con hasta 1,8x de mejora en cargas de trabajo agénticas y hasta 30x de throughput frente a Grace Blackwell en escenarios de interactividad específicos.
*Fuente: [AI News](https://www.artificialintelligence-news.com/)*

**Los agentes de IA ya consumen más tokens que los humanos**
Datos de OpenRouter apuntan a que los agentes autónomos generan ya más tráfico de tokens que los usuarios humanos, forzando a los proveedores a repensar coste, capacidad y fiabilidad de su infraestructura.
*Fuente: [IA en Español](https://iaenespanol.substack.com/p/podcast-ep70-el-resumen-semanal-de)*

**DeepSeek plantea precios de API con descuento en horas valle**
DeepSeek estudiaría precios reducidos de API durante fines de semana y horas de baja demanda, reduciendo a la mitad las facturas de algunos clientes en un contexto de fuerte presión de cómputo.
*Fuente: [IA en Español](https://iaenespanol.substack.com/p/podcast-ep70-el-resumen-semanal-de)*

**Ronda de modelos: Grok 4.6, Qwen3.8 Max, GLM-5.2 Turbo y más**
Agosto ha sido un mes cargado de lanzamientos: Grok 4.6 (xAI, 6 de agosto), Qwen3.8 Max y Qwen Image 3.0 (Alibaba, 2 y 5 de agosto), Seedance 2.5 (ByteDance, 8 de agosto) y GLM-5.2 Turbo (Z.AI, 17 de agosto), entre otros. En total, 12 modelos nuevos de 7 proveedores distintos durante el mes.
*Fuente: [LLM Gateway](https://llmgateway.io/timeline), [Router.one](https://router.one/blog/new-llm-models-august-2026)*

**DARPA completa el primer vuelo real de un F-16 controlado por IA**
La agencia de defensa estadounidense DARPA completó el primer vuelo real de un caza F-16 controlado íntegramente por inteligencia artificial, un hito relevante para la aviación de combate autónoma.
*Fuente: [AI News This Week](https://medium.com/@davidakpovi/ai-news-week-of-august-10-16-2026-af52646d84d2)*

**OpenAI gana terreno frente a Anthropic en el mercado empresarial**
A pesar del fuerte crecimiento de Anthropic, OpenAI estaría ganando cuota en el segmento empresarial. Ambos laboratorios enfrentan un problema de retención de clientes, que cambian de proveedor con cada nuevo lanzamiento de modelo.
*Fuente: [The AI Insider](https://theaiinsider.tech/2026/08/24/the-week-ahead-in-ai-nvidia-earnings-ai-backlash-alibaba-10b-ai-funding-plus-upcoming-earnings-events/)*

**Legora, startup legal impulsada por IA, se acerca a los 10.000 millones de valoración**
La firma sueca de IA legal Legora estaría en proceso de levantar capital a una valoración superior a los 10.000 millones de dólares, frente a los 5.600 millones de hace apenas cuatro meses, con ingresos recurrentes anuales creciendo un 50% en el segundo trimestre hasta unos 150 millones.
*Fuente: [IA en Español](https://iaenespanol.substack.com/p/podcast-ep70-el-resumen-semanal-de)*

**El debate legal sobre entrenamiento con obras protegidas sigue sin resolverse**
Los tribunales continúan sopesando el uso legítimo ("fair use") frente a los derechos de los creadores en el entrenamiento de grandes modelos de lenguaje con literatura protegida por derechos de autor, sin que exista aún un marco claro.
*Fuente: [The AI Insider](https://theaiinsider.tech/2026/08/24/the-week-ahead-in-ai-nvidia-earnings-ai-backlash-alibaba-10b-ai-funding-plus-upcoming-earnings-events/)*

## Conclusiones y tendencias del período

1. **De la capacidad a la confianza.** La narrativa de la semana gira en torno a demostrar el origen y la veracidad del contenido generado por IA (marcas de agua, procedencia, cumplimiento normativo), más que a anunciar nuevos récords de tamaño de modelo.
2. **Presión regulatoria real y con efectos prácticos.** La entrada en vigor del artículo 50 del AI Act europeo el 2 de agosto ya está forzando cambios concretos en el etiquetado de contenido generado por IA en modelos que operan en la UE.
3. **La seguridad frena el ritmo de lanzamientos.** La pausa de OpenAI en el entrenamiento de "Astra" por riesgos cibernéticos muestra que los laboratorios líderes están dispuestos a ralentizar el desarrollo cuando detectan capacidades peligrosas, un cambio notable respecto a la carrera de lanzamientos de años anteriores.
4. **La economía de los agentes ya es dominante.** Los agentes de IA superan a los humanos en consumo de tokens, lo que está reconfigurando los modelos de precios (como el ajuste de DeepSeek) y las prioridades de infraestructura de los grandes proveedores de cómputo.
5. **Consolidación financiera del sector.** Los datos de ingresos de Anthropic, la ronda de Alibaba y el posible aterrizaje de Nvidia en el capital de Perplexity confirman que el mercado sigue canalizando cantidades masivas de capital hacia la infraestructura y los modelos de IA, pese a las dudas sobre retención de clientes empresariales.
