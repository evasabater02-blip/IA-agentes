Ejecuta la rutina semanal de noticias de IA. Sigue estos pasos en orden:

1. Ejecuta el script Python:
```
cd /home/user/IA-agentes/routines && python main.py news
```

2. Cuando termine, lee el archivo `routines/reports/posts_latest.json` para obtener los 2 posts de LinkedIn generados.

3. Crea un borrador de email en Gmail usando el conector MCP de email con:
   - Asunto: "Posts LinkedIn IA - Semana [número de semana]"
   - Cuerpo con ambos posts bien formateados, separados y listos para copiar
   - Incluye el post #1 (noticia más impactante) y el post #2 (perspectiva alternativa)

4. Confirma al usuario que el borrador está creado y dónde encontrarlo en Gmail.
