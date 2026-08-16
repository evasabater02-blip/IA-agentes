# Informe Semanal de Inteligencia Artificial — Semana 33, 2026 (10–16 de agosto)

## Resumen ejecutivo

La semana ha estado marcada por la entrada en vigor efectiva del Reglamento Europeo de IA (AI Act): desde el 2 de agosto, las obligaciones de transparencia del Artículo 50 aplican a cualquier empresa que use IA generativa, exigiendo etiquetado de contenido sintético, aviso claro cuando el usuario interactúa con un chatbot y formación mínima obligatoria para empleados que usen estas herramientas. En paralelo, en EE. UU. el sector privado avanza en autorregulación: Jamie Dimon (JPMorgan) está ampliando la Alianza para Infraestructura Crítica con más de 40 organizaciones de banca, energía y transporte para coordinar enfoques de gobernanza de riesgos de IA.

En el plano de seguridad, OpenAI pausó el desarrollo interno de su modelo Astra tras detectar que podría ser capaz de desarrollar exploits de día cero de forma autónoma, activando por primera vez el umbral "Crítico" de su Preparedness Framework — un hito relevante para el debate sobre capacidades peligrosas emergentes. Como contrapunto, DARPA completó el primer vuelo real de un F-16 controlado íntegramente por IA, mostrando hasta dónde ha llegado la autonomía en entornos de alto riesgo.

En el terreno comercial y de producto, Anthropic reportó ingresos trimestrales de 10.900 millones de dólares (+130% interanual) y su primer beneficio operativo (559 M$), dos años antes de lo previsto, mientras ChatGPT superó los mil millones de usuarios activos semanales. OpenAI recortó un 80% el precio de su modelo GPT 5.6 Luna, abaratando drásticamente las cargas de trabajo vía API. En modelos abiertos, Meta liberó Muse Glimmer (30B, Apache 2.0, ejecutable en una GPU de 24GB) y Alibaba lanzó Qwen 3.8 27B, también Apache 2.0, con contexto nativo de 262K tokens (ampliable a 1M).

## Noticias destacadas

### 1. AI Act: entra en vigor la transparencia obligatoria
El 2 de agosto de 2026 entraron en aplicación las obligaciones del Artículo 50 del Reglamento Europeo de IA: etiquetado de contenido generado artificialmente, aviso obligatorio al usuario cuando interactúa con un chatbot y formación mínima obligatoria para empleados de empresas que usan IA generativa.
**Fuente:** [AI Act: qué cambia el 2 de agosto de 2026](https://iaregulacion.com/ai-act-2-agosto-2026/), [Evolve](https://evolve.es/blog/tech-enablement/2-de-agosto-2026-cambio-reglas-ia/)

### 2. Banca y grandes empresas de EE. UU. coordinan gobernanza de IA
Jamie Dimon (JPMorgan Chase) amplía la Alianza para Infraestructura Crítica, invitando a más de 40 organizaciones de banca, energía, transporte y telecomunicaciones a desarrollar enfoques compartidos de gestión de riesgos de IA.
**Fuente:** [Noticias ONU](https://news.un.org/es/story/2026/07/1541630)

### 3. OpenAI pausa el desarrollo de Astra por riesgo de ciberseguridad crítico
OpenAI detuvo internamente el desarrollo de su modelo Astra el 7 de agosto tras evaluaciones que sugieren capacidad autónoma para desarrollar exploits de día cero, el primer modelo en activar el umbral "Crítico" de su Preparedness Framework.
**Fuente:** [AI Trendssetter](https://aitrendssetter.com/ai-news-this-week-breakthroughs-launches-august-2026/)

### 4. DARPA vuela un F-16 controlado íntegramente por IA
La Agencia de Proyectos de Investigación Avanzada de Defensa de EE. UU. completó el primer vuelo real de un caza F-16 pilotado enteramente por inteligencia artificial.
**Fuente:** [AI Trendssetter](https://aitrendssetter.com/ai-news-this-week-breakthroughs-launches-august-2026/)

### 5. Anthropic anuncia su primer beneficio operativo
Anthropic reportó ingresos de 10.900 millones de dólares en el segundo trimestre de 2026 (+130% interanual) y su primer beneficio operativo (559 M$), dos años antes de lo previsto en su hoja de ruta.
**Fuente:** [AI Trendssetter](https://aitrendssetter.com/ai-news-this-week-breakthroughs-launches-august-2026/)

### 6. ChatGPT supera los mil millones de usuarios activos semanales
OpenAI confirmó que ChatGPT ha superado aproximadamente los mil millones de usuarios activos semanales a principios de agosto, consolidando su posición como el asistente de IA más usado del mundo.
**Fuente:** [AI Trendssetter](https://aitrendssetter.com/ai-news-this-week-breakthroughs-launches-august-2026/)

### 7. OpenAI abarata un 80% el precio de GPT 5.6 Luna
OpenAI redujo aproximadamente un 80% el coste de los tokens de entrada de su modelo GPT 5.6 Luna, facilitando el acceso a cargas de trabajo de gran volumen vía API.
**Fuente:** [AI Trendssetter](https://aitrendssetter.com/ai-news-this-week-breakthroughs-launches-august-2026/)

### 8. Meta libera Muse Glimmer, un modelo abierto de 30B
Meta publicó en código abierto Muse Glimmer, un modelo de 30.000 millones de parámetros bajo licencia Apache 2.0 que puede ejecutarse en una sola GPU de 24GB mediante Ollama o llama.cpp, sin necesidad de nube.
**Fuente:** [AI News This Week (Medium)](https://medium.com/@davidakpovi/ai-news-week-of-august-3-9-2026-8dfa677ffca3)

### 9. Alibaba lanza Qwen 3.8 27B con contexto de hasta 1M de tokens
El equipo Qwen de Alibaba lanzó Qwen 3.8 27B bajo licencia Apache 2.0, un modelo con capacidades de visión integradas, contexto nativo de 262K tokens (ampliable a 1M) y una arquitectura híbrida Gated DeltaNet + Gated Attention.
**Fuente:** [AI News This Week (Medium)](https://medium.com/@davidakpovi/ai-news-week-of-august-3-9-2026-8dfa677ffca3)

### 10. Nvidia consolida su familia Nemotron 3
La familia Nemotron 3 de Nvidia, con arquitectura híbrida Mamba-Transformer MoE orientada a agentes e inferencia eficiente en contexto largo, completa su despliegue: Nano ya disponible, Super y Ultra lanzados en marzo de 2026.
**Fuente:** [PromptQuorum — LLM locales 2026](https://www.promptquorum.com/es/local-llms/local-llm-model-updates-2026)

### 11. Anthropic amplía su catálogo con Claude Fable 5 y Claude Opus 5
Anthropic introdujo en 2026 una nueva clase de modelos "Mythos": Claude Fable 5 (disponibilidad general) y Claude Mythos 5 (uso restringido para defensa cibernética), seguidos por el lanzamiento de Claude Opus 5 el 24 de julio.
**Fuente:** búsqueda "nuevos modelos LLM lanzamiento 2026"

### 12. Primera película generada íntegramente con IA se presenta en Nueva York
Una empresa de generación de vídeo con IA presentó el 10 de agosto "The Cully Hill Boys", un largometraje de 110 minutos generado íntegramente por inteligencia artificial, marcando un hito en la producción audiovisual sintética.
**Fuente:** búsqueda "IA empresas tecnología novedades agosto 2026"

### 13. La IA agéntica se consolida como tendencia dominante de 2026
Según proyecciones citadas esta semana, hasta el 40% de las aplicaciones empresariales podrían incorporar agentes de IA capaces de actuar de forma autónoma —sin esperar aprobación humana en cada paso— antes de que termine el año.
**Fuente:** búsqueda "machine learning avances recientes 2026"

### 14. Los State Space Models (Mamba) ganan terreno frente a los Transformers
Arquitecturas de espacio de estados como Mamba, con complejidad lineal O(n) frente a la cuadrática O(n²) de los Transformers, se consolidan como alternativa eficiente para contextos largos, ya integradas en modelos como Nemotron 3 y Qwen 3.8.
**Fuente:** búsqueda "machine learning avances recientes 2026"

## Conclusiones y tendencias del período

1. **La regulación deja de ser teórica.** Con el AI Act plenamente exigible en la UE, agosto de 2026 marca el paso de la IA "sin reglas" a un marco de cumplimiento obligatorio: transparencia, etiquetado y formación ya no son opcionales para las empresas europeas.
2. **La seguridad de modelos frontera entra en zona crítica.** La pausa de OpenAI en Astra es la primera vez que un modelo activa el nivel "Crítico" de un framework de seguridad interno, señal de que las capacidades autónomas de ciberataque ya no son hipotéticas.
3. **El código abierto sigue empujando la frontera de eficiencia.** Meta y Alibaba compiten por ofrecer modelos potentes ejecutables en hardware de consumo, con arquitecturas híbridas (Mamba + Attention) que reducen el coste de contextos largos.
4. **La economía de la IA madura.** Anthropic alcanza beneficio operativo antes de lo previsto y OpenAI abarata drásticamente sus precios: la fase de quema de caja está dando paso a modelos de negocio más sostenibles.
5. **La autonomía se normaliza en dominios de alto riesgo**, desde caza militares pilotados por IA hasta agentes empresariales que actúan sin supervisión directa, reforzando la urgencia de la gobernanza coordinada entre sector público y privado.
