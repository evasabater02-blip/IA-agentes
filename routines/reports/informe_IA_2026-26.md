# Informe Semanal de Inteligencia Artificial
## Semana 26 de 2026 · 16–22 de junio de 2026

---

## Resumen ejecutivo

La semana del 16 al 22 de junio de 2026 ha sido una de las más convulsas del año en el ecosistema de la IA. El hecho más disruptivo fue la decisión del gobierno de EE.UU. de emitir una directiva de control de exportaciones que obligó a Anthropic a suspender el acceso a sus modelos Claude Fable 5 y Mythos 5 para todos los ciudadanos extranjeros, dentro y fuera del territorio estadounidense, marcando un hito sin precedentes en la regulación gubernamental de modelos de frontera. A esta noticia se sumó la megaoperación de SpaceX, que cerró la adquisición de Cursor por 60.000 millones de dólares en acciones, apenas cuatro días después de su espectacular OPV en el Nasdaq.

En el plano del talento, OpenAI ejecutó uno de sus fichajes más estratégicos de la historia al contratar a Noam Shazeer —coautor de "Attention Is All You Need" y colíder de Gemini en Google— como responsable de Investigación en Arquitecturas. El movimiento sacude a toda la industria y refuerza la posición de OpenAI mientras prepara su propia salida a bolsa, con una valoración que podría alcanzar el billón de dólares. En el frente de los modelos, MiniMax M3 y NVIDIA Nemotron 3 Ultra ampliaron la oferta de modelos open-weight de alto rendimiento, mientras la presión regulatoria europea se intensifica con el vencimiento del 2 de agosto del EU AI Act.

Las tendencias de la semana confirman que la IA ha pasado definitivamente de la fase experimental a la fase de despliegue operativo y choque con la geopolítica: los controles de exportación, las OPV tecnológicas y las regulaciones marcan el nuevo terreno de juego.

---

## Noticias destacadas

### 1. EE.UU. ordena a Anthropic suspender Fable 5 y Mythos 5 para extranjeros
**Fecha:** 12–13 de junio de 2026  
**Impacto:** ★★★★★

El Gobierno de EE.UU. emitió una directiva de control de exportaciones que obligó a Anthropic a desactivar el acceso a Claude Fable 5 y Claude Mythos 5 para todos los nacionales extranjeros, incluyendo los propios empleados extranjeros de Anthropic. La justificación oficial invoca un posible método de "jailbreak" que permitiría eludir las salvaguardas de ciberseguridad del modelo. Anthropic describió el problema como estrecho y señaló que no ha recibido documentación escrita detallada que respalde la posición gubernamental. Los modelos restantes (Opus 4.8 y versiones anteriores) permanecen activos. Anthropic espera restablecer el acceso en los próximos días desde su nueva oficina en Seúl.

**Es la primera vez en la historia que EE.UU. aplica controles de exportación a un modelo de IA de frontera específico.**

> Fuente: [Fortune](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/) · [Al Jazeera](https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals) · [National Law Review](https://natlawreview.com/article/ai-company-anthropic-suspends-access-claude-fable-5-claude-mythos-5-following-us)

---

### 2. SpaceX adquiere Cursor por 60.000 millones de dólares
**Fecha:** 16 de junio de 2026  
**Impacto:** ★★★★★

SpaceX firmó un acuerdo para adquirir Anysphere —empresa detrás del editor de código Cursor— por 60.000 millones de dólares en acciones, solo cuatro días después de su OPV récord en el Nasdaq. Cursor genera más de 4.000 millones de dólares de ARR, cuenta con más de un millón de usuarios de pago y está desplegado en el 64% de las empresas Fortune 500. El cierre de la operación está previsto para el tercer trimestre. Cabe recordar que SpaceX ya había absorbido xAI (Grok) en febrero de 2026, consolidando así un ecosistema de IA propio que ahora incluye el superordenador Colossus y la plataforma X.

> Fuente: [TechCrunch](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-16/spacex-cements-60-billion-deal-to-take-over-ai-startup-cursor) · [CNBC](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html)

---

### 3. Noam Shazeer, coinventor del Transformer, ficha por OpenAI
**Fecha:** 18 de junio de 2026  
**Impacto:** ★★★★★

Noam Shazeer, coautor del paper "Attention Is All You Need" (2017) que sentó las bases de la arquitectura Transformer, y hasta ahora colíder de los modelos Gemini en Google, anunció su incorporación a OpenAI como Lead for Architecture Research. Sam Altman confirmó que este fichaje era un objetivo prioritario desde hace más de una década. El movimiento coincide con el momento en que OpenAI ha presentado confidencialmente su S-1 ante la SEC y trabaja con Goldman Sachs y Morgan Stanley en una OPV que podría valorar la compañía en hasta un billón de dólares.

> Fuente: [CNBC](https://www.cnbc.com/2026/06/18/google-gemini-co-lead-noam-shazeer-leaves-for-openai.html) · [La Nación](https://www.lanacion.com.ar/economia/IA/noam-shazeer-referente-de-ia-de-google-deja-la-compania-para-unirse-a-openai-nid19062026/)

---

### 4. MiniMax M3: el primer modelo open-weight con vídeo nativo y 1M de tokens de contexto
**Fecha:** 1 de junio de 2026  
**Impacto:** ★★★★☆

MiniMax lanzó M3, el primer modelo de código abierto que procesa texto, imágenes y vídeo como entrada nativa, con una ventana de contexto de un millón de tokens. Puntuó 59,0% en SWE-bench Pro, superando el 58,6% de GPT-5.5. El modelo está orientado a codificación y trabajo agéntico y fue preentrenado con más de 100 billones de tokens en un pipeline multimodal desde cero.

> Fuente: [CodingFleet](https://codingfleet.com/blog/minimax-m3-vs-deepseek-v4-pro-the-open-weight-chinese-ai-showdown/)

---

### 5. FERC ordena acelerar la conexión de centros de datos IA a la red eléctrica
**Fecha:** 18 de junio de 2026  
**Impacto:** ★★★★☆

La Comisión Federal Reguladora de Energía de EE.UU. (FERC) emitió una orden a los operadores regionales de la red eléctrica para que defiendan sus marcos de interconexión actuales o propongan reformas que permitan a los centros de datos de IA conectarse más rápido mientras se mantiene la fiabilidad. La demanda energética de la IA se convierte en un factor de política energética nacional.

> Fuente: [BuildFastWithAI](https://www.buildfastwithai.com/blogs/ai-news-today-june-21-2026)

---

### 6. OpenAI prepara OPV con valoración de hasta un billón de dólares
**Fecha:** Semana del 16 de junio de 2026  
**Impacto:** ★★★★☆

OpenAI ha presentado confidencialmente su S-1 ante la SEC y trabaja con Goldman Sachs y Morgan Stanley en una potencial salida a bolsa que podría valorar la compañía en hasta un billón de dólares. La incorporación de Shazeer se produce precisamente en este momento estratégico.

> Fuente: [MLQ News](https://mlq.ai/news/openai-hires-transformer-co-inventor-noam-shazeer-away-from-google-deepmind/)

---

### 7. Cuenta atrás para el EU AI Act: 2 de agosto de 2026
**Fecha:** En vigor · Deadline 02/08/2026  
**Impacto:** ★★★★☆

A menos de 45 días del 2 de agosto de 2026, las obligaciones de transparencia del Reglamento Europeo de IA entran en plena aplicación. Las empresas deben garantizar la formación de su personal en IA, clasificar sus sistemas según nivel de riesgo y cumplir con las normas de transparencia. Las multas pueden alcanzar los 35 millones de euros o el 7% de la facturación global anual. Las obligaciones para sistemas de alto riesgo específicos se han retrasado a diciembre de 2027.

> Fuente: [REPLAI](https://replai.net/eu-ai-act-empresas-obligaciones-agosto-2026/) · [Javadex](https://www.javadex.es/blog/eu-ai-act-guia-cumplimiento-empresas-espanolas-agosto-2026)

---

### 8. Reuters Institute: el 10% de los usuarios ya usa IA para informarse semanalmente
**Fecha:** Junio 2026  
**Impacto:** ★★★☆☆

El Reuters Institute Digital News Report 2026 revela que el 10% de las personas a nivel global usa chatbots de IA (ChatGPT, Perplexity, Gemini) para informarse cada semana, frente al 7% del año anterior. Por primera vez, las redes sociales se han convertido en la fuente principal de noticias a nivel global. Solo el 4% de los usuarios de IA para noticias hace clic en la fuente original.

> Fuente: [El Observador](https://www.elobservador.com.uy/estados-unidos/sociedad/redes-sociales-como-fuente-principal-noticias-y-mayor-uso-la-ia-las-claves-del-informe-2026-del-reuters-institute-n6047966)

---

### 9. DES 2026: la IA ya no es un piloto, es negocio
**Fecha:** 9–11 de junio de 2026  
**Impacto:** ★★★☆☆

El Digital Enterprise Show 2026 cerró con 17.733 profesionales, más de 600 expertos, 403 empresas expositoras y más de 700 innovaciones presentadas. El mensaje dominante: el ciclo de los pilotos se agota; la conversación se ha desplazado a cómo convertir la IA en resultados medibles y sostenibles. Las pymes que no integren IA quedan en desventaja competitiva.

> Fuente: [Precognis](https://www.precognis.com/blog/des-2026-inteligencia-artificial-transformacion-digital-pymes/)

---

### 10. NVIDIA NIM: más de 20 modelos gratuitos con límite de 40 req/min
**Fecha:** Junio 2026  
**Impacto:** ★★★☆☆

NVIDIA NIM ofrece acceso gratuito a más de 20 modelos en su plataforma, incluyendo DeepSeek V4 Flash, Gemma 4 31B, Qwen 3-Next y la familia Nemotron, con un límite de 40 peticiones por minuto. El ecosistema open-weight sigue creciendo y democratizando el acceso a modelos de frontera.

> Fuente: [Prompt Quorum](https://www.promptquorum.com/es/local-llms/top-open-source-models-ollama)

---

## Conclusiones y tendencias del período

### 1. La IA entra en la geopolítica: los controles de exportación han llegado
La suspensión de Fable 5 y Mythos 5 marca un antes y un después. Por primera vez, el gobierno de EE.UU. trata a un modelo de lenguaje como un activo estratégico sujeto a controles de exportación, igual que los semiconductores. Esta tendencia se intensificará: los modelos de frontera serán cada vez más objeto de regulación geopolítica.

### 2. Consolidación del ecosistema: las grandes OPV y adquisiciones reconfiguran el mapa
SpaceX+Cursor+xAI forman un gigante vertical en IA y software de productividad. OpenAI se prepara para una OPV histórica. El mercado se concentra en actores que integran hardware, software e infraestructura.

### 3. El talento es el campo de batalla más caliente
El fichaje de Shazeer por OpenAI, procedente de Google, ilustra que la guerra por los investigadores de élite es tan estratégica como la carrera de modelos. Los autores del Transformer original siguen siendo los activos más codiciados de la industria.

### 4. Open-weight vs. propietario: se estrecha la brecha de rendimiento
MiniMax M3 superó a GPT-5.5 en SWE-bench Pro siendo open-weight. Los modelos chinos y los de código abierto siguen acortando distancias con los modelos propietarios de frontera, lo que presiona los precios a la baja y democratiza el acceso.

### 5. La regulación europea presiona el reloj
Con el EU AI Act a menos de 45 días de su aplicación plena en transparencia, las empresas europeas (y las no europeas que operan en la UE) deben acelerar sus planes de cumplimiento. La ventana para actuar sin presión es muy estrecha.

---

*Informe generado el 22/06/2026 · Fuentes: Fortune, Al Jazeera, TechCrunch, Bloomberg, CNBC, La Nación, Reuters Institute, Digital Enterprise Show 2026, Javadex, REPLAI, MLQ News, CodingFleet, Prompt Quorum.*
