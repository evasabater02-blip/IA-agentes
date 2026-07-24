# Informe Semanal de Inteligencia Artificial — Semana 30 de 2026 (13–24 de julio)

## Resumen ejecutivo

La semana ha estado marcada por una nueva oleada de lanzamientos de modelos frontera y por la aceleración de la carrera comercial entre los grandes laboratorios. OpenAI completó el despliegue público de su familia GPT-5.6 (Sol, Terra y Luna), tras un retraso solicitado por las autoridades regulatorias, mientras que Google adelantó la disponibilidad general de Gemini 3.5 Pro —con una ventana de contexto de 2 millones de tokens y modo de razonamiento "Deep Think"— y lanzó además Gemini 3.6 Flash y Gemini 3.5 Flash Lite para casos de uso más ligeros. xAI, por su parte, presentó Grok 4.5, su primer modelo "Opus-class" entrenado conjuntamente con Cursor, intensificando la competencia en modelos orientados a programación agéntica.

En el plano regulatorio y geopolítico, el Departamento de Comercio de EE. UU. levantó las restricciones de exportación que impedían a ciudadanos extranjeros acceder a determinados modelos avanzados, y el Panel Científico Internacional Independiente sobre IA de la ONU advirtió de que el desarrollo tecnológico sigue avanzando más rápido de lo que los marcos regulatorios pueden absorber. A nivel corporativo, destaca la adquisición por parte de SAP de Prior Labs (especialista en modelos fundacionales tabulares) con un compromiso de inversión superior a 1.000 millones de euros en cuatro años, y el Patch Tuesday más grande de la historia de Microsoft (570 vulnerabilidades corregidas), que la compañía atribuyó al uso intensivo de IA para el descubrimiento de fallos en su propio código.

En conjunto, la semana confirma tres tendencias de fondo: la consolidación de familias de modelos multi-tamaño (flagship / equilibrado / económico) como estrategia comercial estándar, la expansión de la IA generativa hacia edición de vídeo e imagen en tiempo real, y una brecha creciente entre la velocidad de innovación y la capacidad de gobernanza de los reguladores.

## Noticias destacadas

1. **OpenAI lanza la familia GPT-5.6 (Sol, Terra, Luna)**
   OpenAI hizo pública su nueva generación de modelos el 9 de julio, con tres variantes según potencia y coste: Sol (insignia), Terra (uso diario) y Luna (rápido y económico). El lanzamiento se había pospuesto desde finales de junio a petición de las autoridades. *Fuente: DiarioBitcoin / AIToolsRecap.*

2. **Gemini 3.5 Pro alcanza disponibilidad general**
   Google lanzó Gemini 3.5 Pro con ventana de contexto de 2 millones de tokens y modo de razonamiento avanzado "Deep Think", además de las variantes ligeras Gemini 3.6 Flash y Gemini 3.5 Flash Lite. *Fuente: AIapps / BuildFastWithAI.*

3. **Grok 4.5 de xAI, primer modelo entrenado junto a Cursor**
   xAI presentó Grok 4.5 como su modelo "Opus-class", el primero de la serie Grok co-entrenado con Cursor, reforzando su apuesta por la programación agéntica. *Fuente: AIToolsRecap.*

4. **EE. UU. levanta restricciones de exportación de IA**
   El Departamento de Comercio eliminó, con efecto desde el 1 de julio, las restricciones que impedían a ciudadanos extranjeros acceder a determinados modelos avanzados. *Fuente: BuildFastWithAI.*

5. **SAP adquiere Prior Labs por más de 1.000 millones de euros**
   SAP completó la compra de Prior Labs, especializada en modelos fundacionales para datos tabulares, con un plan de inversión de cuatro años para convertirla en un laboratorio de IA de primer nivel. *Fuente: BuildFastWithAI.*

6. **Panel de la ONU advierte sobre el ritmo de la IA frente a la regulación**
   El Panel Científico Internacional Independiente sobre IA de Naciones Unidas publicó un informe preliminar señalando que el avance tecnológico supera la capacidad de los gobiernos para regularlo. *Fuente: Noticias ONU.*

7. **Microsoft registra el mayor Patch Tuesday de su historia**
   La actualización de seguridad de julio corrigió 570 vulnerabilidades (59 críticas), un volumen que Microsoft atribuye al uso intensivo de IA para detectar fallos en su propio código. *Fuente: Reviblog.*

8. **Nuevos modelos open source y de código**
   Moonshot AI lanzó Kimi K3 (16 de julio) y Kimi K2.7 Code enfocado en programación; Tencent liberó Hunyuan 3.0, un modelo MoE de 295B de parámetros totales (21B activos); Poolside presentó Laguna XS 2.1 para programación agéntica. *Fuente: LLM-Stats / TechSy.*

9. **OpenAI presenta modelos de voz full-duplex**
   GPT-Live-1 y GPT-Live-1 mini permiten hablar y escuchar de forma simultánea, un paso relevante hacia asistentes de voz más naturales. *Fuente: Reviblog.*

10. **Google Africa Applied AI Lab**
    Google inauguró en Accra un laboratorio dedicado a apoyar a investigadores y emprendedores africanos con acceso temprano a sus tecnologías de IA. *Fuente: AIapps.*

11. **Edición de vídeo generativa con GPT Image 2 y Aleph 2.0**
    Nueva capacidad que permite editar una sola imagen de referencia y propagar los cambios automáticamente a todo un vídeo, simplificando la posproducción para creadores y estudios. *Fuente: AIapps.*

12. **Apple Intelligence aprobado en China con el modelo Qwen de Alibaba**
    La integración permitirá a Apple ofrecer funciones de IA en el mercado chino apoyándose en el modelo de Alibaba, dada la restricción sobre proveedores extranjeros. *Fuente: Reviblog.*

13. **Meta actualiza el etiquetado de anuncios generados con IA**
    Facebook e Instagram identificarán ahora las promociones creadas o significativamente editadas con IA generativa, en línea con la presión regulatoria sobre transparencia publicitaria. *Fuente: BuildFastWithAI.*

14. **Microsoft lanza VS Code 1.128 con sesiones multi-chat**
    La nueva versión permite mantener varias conversaciones en paralelo con Copilot, que además alcanzó disponibilidad general para Copilot Vision (adjuntar imágenes y PDFs al chat). *Fuente: Reviblog.*

## Conclusiones y tendencias

- **Familias de modelos por niveles**: OpenAI, Google y xAI consolidan la estrategia de ofrecer variantes flagship, equilibradas y económicas de un mismo modelo, facilitando la adopción según presupuesto y caso de uso.
- **Programación agéntica como campo de batalla**: la colaboración de xAI con Cursor y el lanzamiento de Kimi K2.7 Code muestran que los asistentes de codificación autónomos son ahora una prioridad estratégica para varios laboratorios.
- **Brecha regulatoria persistente**: tanto el informe de la ONU como el levantamiento de restricciones de exportación de EE. UU. reflejan tensiones no resueltas entre velocidad de innovación y marcos de gobernanza.
- **IA como herramienta de ciberseguridad y también de riesgo**: el mayor Patch Tuesday de la historia de Microsoft, impulsado por el uso de IA para detectar vulnerabilidades, ilustra el doble filo de estas tecnologías dentro del propio desarrollo de software.
- **Expansión geográfica**: iniciativas como el Africa Applied AI Lab de Google y la adaptación de Apple Intelligence al mercado chino muestran un impulso claro hacia la diversificación regional de la IA generativa.
