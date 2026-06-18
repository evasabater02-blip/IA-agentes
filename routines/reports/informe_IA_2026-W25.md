# Informe Semanal de Inteligencia Artificial — Semana 25 de 2026
**Período:** 16–18 de junio de 2026 | **Generado el:** 18/06/2026

---

## Resumen Ejecutivo

La semana 25 de 2026 estuvo dominada por un hecho sin precedentes en la historia de la IA: el gobierno de Estados Unidos ordenó a Anthropic desactivar por completo sus modelos Fable 5 y Mythos 5 en todo el mundo, apenas tres días después de su lanzamiento, invocando controles de exportación por seguridad nacional. El evento destapó la fragilidad de las cadenas de dependencia empresarial sobre modelos de terceros y reabrió el debate sobre soberanía tecnológica global.

En paralelo, OpenAI sigue preparando el lanzamiento de GPT-5.6 para finales de junio —con una ventana de contexto de 1,5 millones de tokens—, mientras que DeepSeek V4 Pro, el modelo open source de 1,6 billones de parámetros lanzado en abril, consolida su posición como la alternativa más sólida a los modelos propietarios, con costes un 85% inferiores y rendimientos superiores en benchmarks de codificación.

La tendencia estructural de 2026 se confirma: la IA agentica ha dejado de ser experimental. El 90% de las organizaciones globales aumentará su inversión en IA este año, y los primeros sistemas capaces de ejecutar flujos de trabajo completos de extremo a extremo ya operan en producción. La semana también trajo señales desde Japón, donde tres de sus megabancos (con más de 8 billones de dólares en activos) activaron Claude Mythos vía Project Glasswing, en la primera implementación financiera fuera de EE.UU.

---

## Noticias Destacadas

### 1. 🔴 El gobierno de EE.UU. apaga Fable 5 y Mythos 5 de Anthropic
**Fuentes:** [Fortune](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/) · [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-adviser-david-sacks-says-anthropic-refused-to-fix-fable-5-jailbreak-before-us-export-controls) · [MarkTechPost](https://www.marktechpost.com/2026/06/13/anthropic-disables-claude-fable-5-and-mythos-5-after-us-government-order/)

El 12 de junio de 2026, Anthropic desactivó Fable 5 y Mythos 5 para todos sus usuarios en el mundo, apenas tres días después de su lanzamiento (9 de junio). La orden llegó a las 17:21 ET del Departamento de Comercio de EE.UU., citando autoridades de control de exportaciones y seguridad nacional. El gobierno alegó que existía una técnica de jailbreak capaz de desbloquear las capacidades avanzadas de ciberseguridad del modelo Mythos subyacente. Anthropic defendió que la vulnerabilidad era estrecha y no universal, pero ante la imposibilidad de segmentar en tiempo real a los cientos de millones de usuarios, optó por un apagón global. El 16 de junio, la compañía se reunía con la administración Trump para negociar la vuelta al servicio.

---

### 2. ⚠️ El 16% de las empresas no tiene plan de continuidad si un proveedor de IA cae
**Fuente:** [Snyk Blog](https://snyk.io/blog/fable-mythos-suspension-security-takeaways/)

El apagón de Fable 5 expuso una vulnerabilidad sistémica: una de cada seis empresas que usan IA en producción carece de plan de contingencia ante la caída de su proveedor principal. Cada empresa que usaba Fable 5 en flujos de trabajo productivos perdió acceso inmediatamente y sin previo aviso. El incidente impulsará el debate sobre arquitecturas multi-proveedor y soberanía de IA.

---

### 3. 🌏 Japón activa Claude Mythos en su sistema bancario vía Project Glasswing
**Fuente:** [unrot.co — AI News June 16](https://unrot.co/blogs/ai-news-today-june-16-2026)

El gobierno japonés y sus tres mayores megabancos, con más de 8 billones de dólares en activos bajo gestión, han obtenido acceso al modelo Claude Mythos de Anthropic a través del Project Glasswing. Es el primer despliegue confirmado de Glasswing fuera de instituciones financieras estadounidenses, con implicaciones directas para la adopción de IA en el sector regulado asiático.

---

### 4. 🤖 OpenAI introduce Deployment Simulation para pruebas pre-lanzamiento
**Fuente:** [unrot.co — AI News June 16](https://unrot.co/blogs/ai-news-today-june-16-2026)

El 16 de junio, OpenAI presentó Deployment Simulation, una metodología que reproduce conversaciones históricas reales a través del modelo candidato antes de su lanzamiento. La herramienta busca detectar regresiones de comportamiento y fallos de alineamiento en producción antes de que lleguen a los usuarios, en respuesta al post-mortem público que OpenAI publicó en abril sobre un fallo de alineamiento en GPT-5.5.

---

### 5. 🚀 GPT-5.6 de OpenAI: 1,5M tokens de contexto y lanzamiento inminente
**Fuentes:** [DonWeb Blog](https://blog.donweb.com/gpt-5-6-openai-lanzamiento-junio-contexto-tokens/) · [Cryptopolitan](https://www.cryptopolitan.com/gpt-5-6-rumors-openai-eyes-late-june/)

Los mercados de predicción asignan entre 83% y 89% de probabilidad a un lanzamiento de GPT-5.6 entre el 22 y el 28 de junio. El modelo ampliaría la ventana de contexto a 1,5 millones de tokens (+43% respecto a GPT-5.5) y mejoraría un 10-15% la eficiencia por token. Según informes internos, superaría a Claude Mythos en varios benchmarks de codificación agéntica.

---

### 6. 🌐 DeepSeek V4 Pro: 1,6 billones de parámetros, open source y 85% más barato
**Fuentes:** [Geeky Gadgets](https://www.geeky-gadgets.com/deepseek-4-open-source-ai-release/) · [AlphaMatch](https://www.alphamatch.ai/blog/deepseek-v4-review-2026) · [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

Lanzado el 24 de abril bajo licencia MIT, DeepSeek V4 Pro (1,6T parámetros totales, 49B activos) alcanza un 80,6% en SWE-bench Verified y un contexto de 1M tokens, a $0,87/M de tokens de salida, frente a los $3-4 de sus competidores propietarios. El modelo redefine la ecuación coste-rendimiento del mercado y es especialmente relevante para equipos con restricciones presupuestarias.

---

### 7. 🧠 State Space Models (Mamba) desafían la supremacía de los Transformers
**Fuente:** [gIAn Consulting](https://gianconsulting.cl/machine-learning-trends-2026-preparacion/)

Los modelos de espacio de estados (SSM), liderados por la arquitectura Mamba, están cuestionando la hegemonía de los Transformers con una complejidad computacional lineal O(n) frente al O(n²) cuadrático de la atención estándar. Esto los hace especialmente atractivos para aplicaciones de contexto muy largo y dispositivos edge con recursos limitados.

---

### 8. 🏢 IA Agentica: de la experimentación a la producción empresarial
**Fuentes:** [Microsoft Source EMEA](https://news.microsoft.com/source/emea/features/asi-evolucionara-la-ia-siete-tendencias-a-seguir-en-2026/?lang=es) · [Capgemini](https://www.capgemini.com/us-en/insights/research-library/top-tech-trends-of-2026/)

El 90% de las organizaciones globales planea aumentar su inversión en IA en 2026. Si 2025 fue el año de explorar la IA generativa, 2026 es el año de los agentes operando a escala: sistemas que razonan, planifican y ejecutan tareas complejas de extremo a extremo con intervención humana mínima. Las empresas están pasando de pilotos a despliegues productivos.

---

### 9. 🌍 DES 2026 cierra con soberanía tecnológica e IA operativa como ejes centrales
**Fuente:** [La Ecuación Digital](https://www.laecuaciondigital.com/empresas/eventos/des-2026-ia-soberania-tecnologica-tecnologias-duales/)

El Digital Enterprise Show 2026 cerró su edición centrada en el despliegue operativo de la IA y la dependencia tecnológica. El apagón de Fable 5 —ocurrido durante el propio evento— reforzó en tiempo real el debate sobre la necesidad de alternativas europeas y locales.

---

### 10. 🇲🇽 Congreso IA, Tecnología y Negocios América Digital México 2026
**Fuente:** [Infobae](https://www.infobae.com/america/agencias/2026/06/04/la-ia-entra-en-fase-empresarial-mas-de-5000-ejecutivos-analizaran-su-impacto-en-los-negocios/)

Los días 9 y 10 de junio, más de 5.000 ejecutivos y líderes de innovación de Latinoamérica se reunieron en Ciudad de México para analizar el impacto empresarial de la IA. Participaron Google Cloud, Salesforce, Dell Technologies, Snowflake y L'Oréal, evidenciando la aceleración de la adopción en la región.

---

## Conclusiones y Tendencias del Período

**1. La soberanía de la IA es ahora una cuestión de estado.** El primer apagón de modelos IA por orden gubernamental marca un antes y un después. Las empresas que dependen de un único proveedor de IA en flujos críticos enfrentan un riesgo operacional real que hasta esta semana parecía teórico.

**2. El open source cierra la brecha de rendimiento.** DeepSeek V4 Pro y GLM 5.1 demuestran que el código abierto ya compite de tú a tú con los modelos propietarios, a una fracción del coste. La ecuación de "pagar por el mejor modelo" se complica.

**3. La carrera de contexto no para.** GPT-5.5 → GPT-5.6 en semanas, con un salto del 43% en ventana de contexto. Los documentos largos, bases de código completas y memorias persistentes están a punto de dejar de ser un reto técnico.

**4. La IA agentica es el nuevo campo de batalla.** Todas las grandes apuestas empresariales de 2026 convergen en agentes autónomos. Quien resuelva la fiabilidad y la supervisión humana a escala ganará el ciclo.

**5. Diversificación geográfica de la IA.** Japón, América Latina y Europa aceleran su adopción y buscan soberanía. El ecosistema deja de ser exclusivamente anglosajón.
