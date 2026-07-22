# Informe semanal de Inteligencia Artificial — Semana 30, 2026 (20–26 de julio)

## Resumen ejecutivo

La semana ha confirmado el giro que se veía venir en los últimos meses: la carrera ya no es solo por el modelo más grande, sino por el más útil, barato y fiable de desplegar a escala. OpenAI consolidó la disponibilidad general de su familia GPT-5.6 (Sol, Terra y Luna) tras el aplazamiento de junio, xAI respondió con Grok 4.5 a precios muy agresivos, y Google sigue arrastrando el lanzamiento de Gemini 3.5 Pro tras detectar problemas de calidad en las pruebas empresariales. Mientras tanto, el frente open-source vive su semana más intensa del año, con DeepSeek V4 y los pesos abiertos de Kimi K3 llegando casi en paralelo, además de GLM-5.2 consolidándose como referencia abierta.

En el plano regulatorio e industrial, la Comisión Europea ha emitido órdenes vinculantes a Google para abrir Android a asistentes de IA rivales, el Panel Científico de la ONU sobre IA advierte de que la tecnología avanza más rápido que la capacidad de los gobiernos para regularla, y el gobierno de EE. UU. ha bloqueado el acceso público a su modelo de IA más potente, reservándolo a socios verificados. A nivel empresarial, destaca el fuerte ajuste de plantilla de Oracle (hasta 30.000 empleos) para financiar su expansión en centros de datos de IA, en contraste con el uso creciente y ya normalizado de IA generativa en producción audiovisual (Netflix) y herramientas para desarrolladores (Microsoft, GitHub Copilot).

La tendencia de fondo es clara: los modelos de frontera compiten cada vez más en coste por token y en fiabilidad para tareas agénticas reales, mientras la presión regulatoria y geopolítica sobre el acceso a los modelos más potentes se intensifica.

## Noticias destacadas

1. **OpenAI lanza oficialmente la familia GPT-5.6 (Sol, Terra, Luna)**
   Disponible desde el 9 de julio en ChatGPT, Codex y la API. Sol es el buque insignia (5$/30$ por millón de tokens de entrada/salida) y establece nuevo estado del arte en Terminal-Bench 2.1; Terra y Luna ofrecen versiones más económicas para uso diario y tareas ligeras.
   *Fuente: [AIToolsRecap](https://aitoolsrecap.com/Blog/AINewsJuly2026.aspx), [Kingy.ai](https://kingy.ai/blog/gpt-5-6-sol-vs-claude-fable-5-vs-grok-4-5-vs-muse-spark-1-1/)*

2. **xAI lanza Grok 4.5 con el precio más agresivo del mercado**
   Publicado el 8 de julio, a 2$/6$ por millón de tokens de entrada/salida, posicionándose como la amenaza de coste-eficiencia frente a OpenAI y Google.
   *Fuente: [Tech Insider](https://tech-insider.org/grok-vs-chatgpt-vs-gemini-2026/)*

3. **Gemini 3.5 Pro de Google se retrasa por tercera vez**
   El modelo, anunciado en mayo, sigue sin fecha oficial tras detectarse problemas de calidad en pruebas empresariales; Google baraja una versión "puente" mientras tanto. Se rumorea contexto de 2M de tokens y modo de razonamiento Deep Think reforzado.
   *Fuente: [Tech Times](https://www.techtimes.com/articles/320736/20260716/rebuilt-gemini-35-pro-misses-third-deadline-google-eyes-stopgap-release.htm)*

4. **Semana histórica para los modelos de pesos abiertos**
   DeepSeek V4 se publica el 24 de julio y Moonshot AI libera los pesos de Kimi K3 el 27 de julio, en lo que se describe como la mayor concentración de lanzamientos open-weight del año; GLM-5.2 (Zhipu/Z.ai) se mantiene como referencia del top open-source.
   *Fuente: [Tech Startups](https://techstartups.com/2026/07/20/top-tech-news-today-july-20-2026-alibaba-bezos-blackstone-google-moonshot-ai-nvidia-samsung-more/), [PromptQuorum](https://www.promptquorum.com/es/local-llms/top-open-source-models-ollama)*

5. **La Comisión Europea obliga a Google a abrir Android a asistentes de IA rivales**
   Órdenes vinculantes exigen que los asistentes de terceros aprobados obtengan activación por voz y funcionamiento entre apps, además de acceso parcial a datos de búsqueda de Google.
   *Fuente: [Tech Startups](https://techstartups.com/2026/07/20/top-tech-news-today-july-20-2026-alibaba-bezos-blackstone-google-moonshot-ai-nvidia-samsung-more/)*

6. **La ONU advierte: la IA avanza más rápido que la capacidad regulatoria**
   El Panel Científico Internacional Independiente sobre IA de Naciones Unidas presentó un informe preliminar alertando de que los gobiernos no logran seguir el ritmo de desarrollo de la tecnología.
   *Fuente: [Noticias ONU](https://news.un.org/es/story/2026/07/1541630)*

7. **EE. UU. bloquea el acceso público a su modelo de IA más potente**
   El gobierno estadounidense ha restringido el modelo más avanzado desarrollado hasta la fecha a socios verificados con credenciales aprobadas, sin acceso público.
   *Fuente: [Tech Startups](https://techstartups.com/2026/07/20/top-tech-news-today-july-20-2026-alibaba-bezos-blackstone-google-moonshot-ai-nvidia-samsung-more/)*

8. **Oracle recorta hasta 30.000 empleos para financiar centros de datos de IA**
   El ajuste de plantilla se enmarca en la fuerte inversión de la compañía en infraestructura de IA, reflejando la presión de costes que genera la carrera por capacidad de cómputo.
   *Fuente: [AI in July 2026 — AIGetFree](https://aigetfree.com/ai-news-july-2026-biggest-stories-trends/)*

9. **OpenAI presenta GPT-Live-1 y GPT-Live-1 mini, voz full-duplex**
   Modelos capaces de hablar y escuchar simultáneamente, permitiendo interrupciones naturales; especialmente relevantes para traducción en directo.
   *Fuente: [Reviblog](https://reviblog.net/noticia/noticias-tecnologia-9-julio-2026/)*

10. **Google lanza el Africa Applied AI Lab en Accra**
    Nueva iniciativa para dar a investigadores y emprendedores africanos acceso anticipado a tecnología de Google y asistencia técnica directa, orientada a soluciones adaptadas a los retos del continente.
    *Fuente: [ZoneTechify](https://www.zonetechify.com/blog/ai-news-july-2026-latest-ai-developments)*

11. **Microsoft actualiza VS Code y generaliza Copilot Vision**
    VS Code 1.128 añade sesiones multi-chat en paralelo; Copilot Vision alcanza disponibilidad general, permitiendo adjuntar imágenes y PDFs directamente en el chat.
    *Fuente: [Reviblog](https://reviblog.net/noticia/noticias-tecnologia-9-julio-2026/)*

12. **Netflix confirma el uso extendido de IA generativa en producción**
    La compañía reveló que sus equipos usaron herramientas de IA generativa en aproximadamente 300 títulos durante 2026, principalmente en tareas de postproducción.
    *Fuente: [Reviblog](https://reviblog.net/noticia/noticias-tecnologia-9-julio-2026/)*

13. **Dos grandes laboratorios de IA presentan su salida a bolsa (IPO)**
    En el mismo mes, dos de los principales laboratorios de IA han presentado documentación para salir a bolsa, reflejando la maduración financiera del sector.
    *Fuente: [Tech Startups](https://techstartups.com/2026/07/20/top-tech-news-today-july-20-2026-alibaba-bezos-blackstone-google-moonshot-ai-nvidia-samsung-more/)*

14. **SpaceX muestra un prototipo de dispositivo de IA más fino que un iPhone**
    Presentado a inversores, usa procesador Snapdragon y tecnología de xAI, sumándose a la tendencia de hardware dedicado para asistentes de IA.
    *Fuente: [Reviblog](https://reviblog.net/noticia/noticias-tecnologia-9-julio-2026/)*

15. **La batalla por el liderazgo en IA se traslada al mundo físico**
    Inversiones multimillonarias en nuevos materiales, semiconductores, centros de datos, redes de fibra y sistemas de descubrimiento de fármacos marcan la pauta de julio, más allá del software.
    *Fuente: [Tech Startups](https://techstartups.com/2026/07/20/top-tech-news-today-july-20-2026-alibaba-bezos-blackstone-google-moonshot-ai-nvidia-samsung-more/)*

## Conclusiones y tendencias del período

- **De "más grande" a "más útil y barato":** los tres grandes laboratorios (OpenAI, xAI, Google) compiten ahora tanto en capacidad como en precio por token, con Grok 4.5 marcando el listón más agresivo y Google retrasando su modelo insignia por priorizar calidad sobre velocidad de salida.
- **El open-source acelera:** la llegada casi simultánea de DeepSeek V4, Kimi K3 y GLM-5.2 confirma que la frontera abierta se está cerrando frente a los modelos propietarios, con implicaciones directas en coste de adopción para empresas.
- **La regulación se activa en dos frentes distintos:** Europa presiona por interoperabilidad (caso Google/Android), mientras EE. UU. restringe el acceso a sus modelos más potentes por motivos estratégicos — dos enfoques opuestos que conviven en la misma semana.
- **La IA ya es coste estructural, no solo inversión:** los recortes de plantilla de Oracle para financiar infraestructura de IA anticipan que 2026 será el año en que muchas compañías tengan que elegir entre personal y capacidad de cómputo.
- **La adopción práctica se normaliza:** de Netflix a Microsoft, la IA generativa deja de ser un experimento y pasa a integrarse como herramienta de producción estándar en flujos de trabajo reales.
