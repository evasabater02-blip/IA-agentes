# Informe Semanal de Inteligencia Artificial — Semana 35 de 2026 (24-28 de agosto)

*Generado el 28/08/2026*

## Resumen ejecutivo

Esta semana la industria de la IA ha seguido consolidando dos tendencias que llevan varias semanas ganando peso: la carrera por los agentes de larga duración (capaces de operar horas sin supervisión humana) y el giro hacia la trazabilidad y la seguridad frente a la pura capacidad. Anthropic sigue mostrando un crecimiento financiero extraordinario (ingresos anualizados de 65.000 M$, primer beneficio operativo alcanzado con dos años de adelanto sobre el plan), mientras OpenAI ha optado por pausar el entrenamiento de su próximo modelo, Astra, al detectar posibles capacidades cibernéticas críticas, reforzando sus protocolos de seguridad antes de continuar.

En el plano de la estandarización, el protocolo A2A de Google se ha incorporado formalmente a la Agentic AI Foundation de la Linux Foundation, uniéndose al MCP de Anthropic bajo un mismo paraguas de gobernanza neutral con más de 250 miembros (AWS, Microsoft, Google, Anthropic, OpenAI, entre otros). Esto confirma que 2026 es el año en que la interoperabilidad entre agentes deja de ser una aspiración y empieza a convertirse en infraestructura compartida.

También se ha conocido una vulnerabilidad relevante para la seguridad de los sistemas agénticos: un fallo en las API de OpenAI, Anthropic y Google permitiría que modelos más débiles "descifren" parcialmente el razonamiento interno de modelos más potentes, lo que abre un debate práctico sobre la confidencialidad del razonamiento de los LLM en entornos empresariales.

## Noticias destacadas

**OpenAI pausa el entrenamiento de Astra por riesgo cibernético crítico**
OpenAI detuvo el entrenamiento de su próximo modelo, de nombre en clave Astra, tras detectar indicios de que podría haber alcanzado capacidades cibernéticas críticas, y ha reforzado sus protocolos de seguridad antes de retomarlo.
*Fuente: cobertura agregada de noticias de IA de la semana (iaenespanol.substack.com, evolutivaia.com)*

**Fallo de API permite a modelos débiles "leer" el razonamiento de modelos más potentes**
Investigadores de seguridad han identificado un fallo compartido en las API de OpenAI, Anthropic y Google que permitiría a modelos de IA más débiles decodificar parcialmente el razonamiento interno de modelos más avanzados, con implicaciones para la confidencialidad de los sistemas agénticos empresariales.
*Fuente: [The Hacker News](https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html)*

**Anthropic alcanza 65.000 M$ de ingresos anualizados**
Anthropic reportó ingresos anualizados de 65.000 millones de dólares, sumando 18.000 millones en solo dos meses. En su informe del segundo trimestre declaró 10.900 M$ de ingresos (+130%) y su primer beneficio operativo (559 M$), dos años antes de lo previsto.
*Fuente: cobertura agregada (medium.com/@davidakpovi, iaenespanol.substack.com)*

**El protocolo A2A de Google se integra en la Agentic AI Foundation**
El 20 de agosto, el protocolo A2A de Google se incorporó formalmente a la Agentic AI Foundation (AAIF), dirigida por la Linux Foundation, uniéndose al Model Context Protocol (MCP) de Anthropic bajo la misma gobernanza neutral. La fundación supera ya los 250 miembros, incluidos AWS, Microsoft, Google, Anthropic y OpenAI.
*Fuente: cobertura agregada de noticias de agentes de IA (aiagentstore.ai)*

**Google presenta Gemini 3.7 Flash**
Google lanzó Gemini 3.7 Flash, un modelo optimizado para programación y flujos de trabajo agénticos orientado a ejecutar tareas completas de forma autónoma.
*Fuente: cobertura agregada de noticias de IA de la semana*

**xAI lanza Grok 4.6 centrado en agentes de larga duración**
xAI publicó Grok 4.6 el 12 de agosto, con un precio de 2 $/6 $ por millón de tokens de entrada/salida y una puntuación de 61 en el AA Intelligence Index. La compañía describe el salto respecto a Grok 4.5 como una mejora centrada en tareas de varios pasos que se ejecutan durante horas sin supervisión humana continua.
*Fuente: cobertura agregada de avances en machine learning*

**Anthropic introduce marcas de agua para cumplir la normativa de la UE**
Anthropic ha comenzado a integrar marcas de agua imperceptibles y señales de procedencia en el contenido generado por Claude, en línea con los nuevos requisitos de transparencia de la Unión Europea; los nuevos modelos de Claude lanzados en la UE desde el 2 de agosto ya incorporan este marcado.
*Fuente: cobertura agregada de noticias de IA de la semana*

**Los agentes de IA ya consumen más tokens que los humanos**
Varios análisis de la semana coinciden en que el consumo de tokens por agentes de IA ha superado al de las consultas humanas directas, obligando a los proveedores a repensar el coste, la capacidad de sus infraestructuras y la fiabilidad de los sistemas agénticos.
*Fuente: cobertura agregada de noticias de IA de la semana*

**AWS lleva a producción la búsqueda web en Bedrock AgentCore**
El 21 de agosto, AWS anunció la disponibilidad general de Web Search en Amazon Bedrock AgentCore, una herramienta gestionada del lado del servidor que permite a los agentes obtener conocimiento web citado y actualizado.
*Fuente: cobertura agregada de noticias de agentes de IA (aiagentstore.ai)*

**NVIDIA presenta SparDA, una nueva variante de transformer**
Investigadores de NVIDIA desarrollaron SparDA, una arquitectura que logra una decodificación 1,7 veces más rápida y una mejora de 6,5 puntos en precisión de razonamiento largo respecto a los transformers convencionales.
*Fuente: cobertura agregada de avances en machine learning*

**DARPA completa el primer vuelo real de un F-16 controlado por IA**
La Defense Advanced Research Projects Agency (DARPA) completó el primer vuelo en entorno real de un F-16 controlado íntegramente por inteligencia artificial, un hito relevante para la aviación de combate autónoma.
*Fuente: cobertura agregada de noticias de IA (AI News: Week of August 10-16, 2026)*

**OpenAI gana terreno frente a Anthropic entre usuarios de empresa**
Según datos de Ramp citados por su economista Ara Kharazian, OpenAI está creciendo más rápido que Anthropic entre usuarios empresariales de EE. UU. durante lo que va del tercer trimestre.
*Fuente: [TechCrunch](https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/)*

**OpenAI anuncia mejoras de velocidad de inferencia y nuevas herramientas para desarrolladores**
El 25 de agosto, OpenAI presentó los primeros resultados de "Jalapeño", centrados en velocidad y eficiencia de inferencia, además de un plugin de administración para ChatGPT Work y Codex, y mejoras de precio-rendimiento con GPT-5.6 en Kiro.
*Fuente: cobertura agregada de noticias de OpenAI*

**Apple, Amazon e Intel refuerzan sus apuestas de IA en hardware y asistentes**
Apple presentó una nueva generación de Siri basada en IA, Amazon reveló un robot de almacén inteligente para acelerar entregas, y NVIDIA e Intel anunciaron nuevos chips y alianzas (Foxconn, Echo Neural Technologies) orientados a ejecutar agentes de IA en dispositivos personales.
*Fuente: cobertura agregada de noticias de tecnología empresarial*

## Conclusiones y tendencias del período

La semana confirma que el foco de la industria se está desplazando de "quién tiene el modelo más grande" a "quién puede operar agentes de IA de forma fiable, segura y trazable durante horas sin supervisión". Los lanzamientos de Grok 4.6, Gemini 3.7 Flash y las mejoras de inferencia de OpenAI apuntan todos a la misma dirección: tareas largas y autónomas. En paralelo, la seguridad deja de ser un discurso y se convierte en decisiones operativas concretas, como la pausa de entrenamiento de OpenAI o el hallazgo de una vulnerabilidad compartida entre los tres grandes proveedores de API.

La estandarización también avanza con fuerza: la convergencia de A2A y MCP bajo la misma fundación reduce la fragmentación del ecosistema agéntico y facilita que las empresas construyan integraciones sin apostar por un único proveedor. Y en lo financiero, el crecimiento de Anthropic —con un primer beneficio operativo logrado dos años antes de lo previsto— convive con señales de que OpenAI está recuperando terreno comercial, en un mercado donde la competencia por el cliente empresarial se está intensificando.
