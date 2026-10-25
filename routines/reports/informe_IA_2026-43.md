# Informe semanal de IA — 25/10/2026 (Semana 43)

## Resumen ejecutivo

La semana estuvo marcada por la ciberseguridad: **PHP2Shell**, dos vulnerabilidades críticas de ejecución remota de código en PHP (CVE-2026-109618 y CVE-2026-109619, CVSS 9.2), descubiertas con herramientas de IA, obligaron a PHP a publicar parches de emergencia el 21 de octubre. Es uno de los primeros casos de gran impacto en que agentes de IA encuentran y convierten en explotable un fallo en software ubicuo en semanas, no meses.

En el plano comercial y de infraestructura, OpenAI llevó la publicidad de ChatGPT a 89 países (más de 100.000 anunciantes), Anthropic negocia un contrato de cómputo de unos 45.000 millones de dólares con Nscale, y Google consolidó la disponibilidad general de Gemini 4 Argon. En paralelo, siguen los lanzamientos de modelos más baratos y eficientes (MiniMax M3.1 Flash, Claude Haiku 5.5).

**Nota de fiabilidad:** las búsquedas devolvieron muchas fuentes secundarias con fechas y detalles inconsistentes. Las noticias marcadas como "reportado" no tienen confirmación oficial. No se pudo abrir ninguna página directamente (WebFetch sin acceso de red), por lo que todo se basa en los resúmenes de búsqueda.

## Noticias destacadas

1. **PHP2Shell: la IA encuentra fallos críticos en PHP.** Dos RCE sin autenticación (CVSS 9.2) afectan a una gran parte de la web. Parches en PHP 8.2.35, 8.3.36, 8.4.27 y 8.5.12 (21 oct). Investigadores de Calif, Wiz y OpenAI lo hallaron con IA; se reportó explotación activa aún en investigación. Fuentes: [Wiz](https://wiz.io/blog/php2shell-php-rce), [BleepingComputer](https://bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws).
2. **"Octubre Negro" de ciberataques con IA.** Análisis de la semana sobre PHP2Shell y otros incidentes (ARTEX, Cairn, LiteLLM, Zeabur), distinguiendo lo real de lo exagerado. Fuente: The AI Revolution (theairevolution.info, 23 oct; no verificado directamente).
3. **ChatGPT Ads llega a 89 países.** OpenAI añadió 26 mercados (63 en septiembre); más de 100.000 anunciantes frente a ~20.000 a finales de agosto. Solo en planes Free y Go. Se vincula a una posible salida a bolsa en 2027. Fuente: [The Next Web](https://thenextweb.com/news/chatgpt-ads-89-countries-100000-advertisers).
4. **Anthropic–Nscale: ~45.000 M$ en cómputo.** Contrato reportado de seis años, ~400–460 MW en West Virginia con sistemas NVIDIA Vera Rubin, operativo hacia finales de 2027. Sin anuncio oficial. Fuentes: [W.Media](https://w.media/anthropic-strikes-us-45-billion-ai-compute-deal-with-nscale-reports/), [Sifted](https://sifted.eu/articles/nscale-athropic-deal-data-centre/).
5. **Gemini 4 Argon, disponibilidad general (13 oct).** Contexto de ~1M tokens; API a 2/10 $ por millón de tokens (sube a 4/20 el 30 nov). Google afirma mejoras en agentes de código; las comparativas con otros modelos de frontera no están verificadas de forma independiente. Fuente: [documentación de Google](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=zh-tw).
6. **MiniMax M3.1 Flash (19 oct).** Mejora de 13 puntos en el Artificial Analysis Intelligence Index (hasta 42) a la mitad de coste. Fuente: Café con IA, 20 oct (no verificado directamente).
7. **Anthropic: Claude Duet (research preview, 21 oct).** Aparece en un tracker de lanzamientos; sin más detalle. Fuente: [Evertune AI Model Tracker](https://www.evertune.ai/resources/ai-model-tracker).
8. **OpenAI: GPT-6 Pro — Parallel Agents (16 oct).** Según el mismo tracker; los reportes sobre la gama GPT-6 (Sol, Luna, Astra) son contradictorios. Fuente: [Evertune](https://www.evertune.ai/resources/ai-model-tracker).
9. **NVIDIA Nemotron 3.5 (21 oct).** Mencionado por Noticias IA; no se encontró confirmación adicional.
10. **Panorama competitivo.** Un tracker contabiliza 149 lanzamientos de modelos de 6 proveedores a 21 oct, con actividad reciente de DeepSeek y Meta. Fuente: [pricepertoken.com](https://pricepertoken.com/news/model-releases).

## Conclusiones y tendencias

- **La IA ofensiva y defensiva ya es real:** la reducción del tiempo entre descubrimiento y explotación obliga a acelerar los parches y a usar IA también en defensa.
- **Monetización:** la publicidad en chatbots se escala de forma agresiva como vía de ingresos ante los costes de cómputo.
- **Cómputo como ventaja estratégica:** contratos de decenas de miles de millones y entregas a 2027 marcan la carrera.
- **Presión de precios:** modelos "Flash"/"Haiku" ofrecen más capacidad por menos coste; los precios introductorios (Gemini 4 Argon) son temporales.
- **Cautela con la información:** varias de las noticias de la semana carecen de confirmación oficial; conviene contrastar antes de publicar.
