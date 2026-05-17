Ejecuta la rutina semanal completa de noticias de IA. Sigue estos pasos en orden sin saltarte ninguno:

## Paso 1: Buscar noticias de IA de esta semana

Busca en la web usando las siguientes consultas y recoge los titulares, fuentes y resúmenes más relevantes:
- "inteligencia artificial noticias esta semana"
- "AI news this week 2026"
- "nuevos modelos LLM lanzamiento"
- "machine learning avances recientes"
- "IA empresas tecnología novedades"

Elimina duplicados y quédate con los 10-15 resultados más relevantes e interesantes.

## Paso 2: Generar el informe semanal

Con las noticias encontradas, redacta un informe en Markdown con esta estructura:
- Título con fecha y número de semana
- Resumen ejecutivo (2-3 párrafos)
- Noticias destacadas (título, resumen 2-3 líneas, fuente)
- Conclusiones y tendencias del período

Guarda el informe en: `routines/reports/informe_IA_YYYY-WW.md` (usa el año y semana actuales).

## Paso 3: Generar 2 posts de LinkedIn

**Post #1 — La noticia más impactante:**
- Primera línea gancho que pare el scroll
- 150-250 palabras
- 3-5 puntos clave con saltos de línea
- Pregunta final que invite a comentar
- 3-5 hashtags relevantes
- Tono profesional pero cercano, en español

**Post #2 — Perspectiva alternativa:**
- Enfócate en implicaciones prácticas, un avance menos obvio, o cómo afecta a sectores concretos
- 150-250 palabras
- Tono más reflexivo y analítico
- Dato sorprendente o pregunta provocadora al inicio
- Llamada a la acción concreta al final
- 3-5 hashtags relevantes
- En español

## Paso 4: Guardar los posts

Guarda los dos posts en `routines/reports/posts_latest.json` con este formato exacto:
```json
{
  "generado_el": "DD/MM/YYYY a las HH:MM",
  "semana": "YYYY-WNN",
  "post_1": {
    "titulo": "Noticia más impactante de la semana",
    "contenido": "..."
  },
  "post_2": {
    "titulo": "Perspectiva alternativa / implicaciones prácticas",
    "contenido": "..."
  }
}
```

## Paso 5: Crear borrador de email en Gmail

Usa el conector MCP de Gmail para crear un borrador con:
- **Asunto:** `Posts LinkedIn IA — Semana [número] de [año]`
- **Cuerpo:** Los dos posts bien formateados y separados, listos para copiar y pegar directamente en LinkedIn. Incluye una línea separadora entre ambos y etiqueta claramente cuál es cada uno.

## Paso 6: Confirmar al usuario

Indica:
- Cuántas noticias encontraste
- Dónde está guardado el informe
- Que el borrador de email está creado en Gmail
