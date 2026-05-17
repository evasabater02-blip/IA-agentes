"""
Agente principal que orquesta búsqueda web + resumen con IA.
Genera informes semanales sobre noticias de IA y posts para LinkedIn.
"""

import json
import os
from datetime import datetime
from pathlib import Path

from search_connector import ChromeSearchConnector
from ai_summarizer import AISummarizer
from linkedin_generator import LinkedInGenerator


# Queries para el informe semanal de noticias de IA
QUERIES_NOTICIAS_IA = [
    "inteligencia artificial noticias semana",
    "AI news this week",
    "machine learning avances recientes",
    "LLM nuevos modelos lanzamiento",
    "IA empresas tecnología novedades",
]

DIRECTORIO_INFORMES = Path("reports")
ARCHIVO_POSTS_LATEST = DIRECTORIO_INFORMES / "posts_latest.json"


class AINewsAgent:
    """Agente que busca noticias de IA, genera informes semanales y posts de LinkedIn."""

    def __init__(self):
        self.buscador = ChromeSearchConnector()
        self.resumidor = AISummarizer()
        self.linkedin = LinkedInGenerator()
        DIRECTORIO_INFORMES.mkdir(exist_ok=True)

    def run_weekly_report(self) -> dict:
        """
        Ejecuta el flujo completo semanal:
        1. Busca noticias de IA de la última semana.
        2. Deduplica y resume con Claude.
        3. Genera 2 posts de LinkedIn con enfoques distintos.
        4. Guarda el informe y los posts en reports/.
        5. Retorna rutas de los archivos generados.

        Returns:
            Dict con 'informe', 'posts' (rutas) y el contenido de los posts.
        """
        print("\n" + "=" * 60)
        print("   GENERANDO INFORME SEMANAL DE NOTICIAS IA")
        print("=" * 60)

        todos_los_resultados = []
        urls_vistas = set()

        for i, query in enumerate(QUERIES_NOTICIAS_IA, 1):
            print(f"\n[{i}/{len(QUERIES_NOTICIAS_IA)}] Buscando: '{query}'...")
            resultados = self.buscador.search(query, max_results=5)
            print(f"  → {len(resultados)} resultados encontrados")

            for resultado in resultados:
                url = resultado.get("url", "")
                if url and url not in urls_vistas:
                    urls_vistas.add(url)
                    todos_los_resultados.append(resultado)

        print(f"\n→ Total de resultados únicos: {len(todos_los_resultados)}")

        if not todos_los_resultados:
            print("[!] No se encontraron resultados. Verifica tu conexión a internet.")
            return {}

        print("\n→ Generando informe con Claude...")
        informe = self.resumidor.summarize_news_batch(todos_los_resultados)

        # Guardar informe semanal
        semana = datetime.now().strftime("%Y-W%W")
        nombre_informe = DIRECTORIO_INFORMES / f"informe_IA_{semana}.md"
        encabezado = (
            f"<!-- Informe generado automáticamente el "
            f"{datetime.now().strftime('%d/%m/%Y a las %H:%M')} -->\n"
            f"<!-- Semana: {semana} | Fuentes: {len(todos_los_resultados)} resultados únicos -->\n\n"
        )
        with open(nombre_informe, "w", encoding="utf-8") as f:
            f.write(encabezado + informe)
        print(f"\n✓ Informe guardado en: {nombre_informe}")

        # Generar posts de LinkedIn
        print("\n→ Generando posts de LinkedIn...")
        posts = self.linkedin.generar_dos_posts(informe)

        # Guardar posts (siempre como latest + versión con fecha)
        nombre_posts = DIRECTORIO_INFORMES / f"posts_IA_{semana}.json"
        datos_posts = {
            "generado_el": datetime.now().strftime("%d/%m/%Y a las %H:%M"),
            "semana": semana,
            "informe_ruta": str(nombre_informe),
            "post_1": {
                "titulo": "Noticia más impactante de la semana",
                "contenido": posts["post_1"],
            },
            "post_2": {
                "titulo": "Perspectiva alternativa / implicaciones prácticas",
                "contenido": posts["post_2"],
            },
        }

        with open(nombre_posts, "w", encoding="utf-8") as f:
            json.dump(datos_posts, f, ensure_ascii=False, indent=2)

        # Sobrescribir latest para acceso rápido
        with open(ARCHIVO_POSTS_LATEST, "w", encoding="utf-8") as f:
            json.dump(datos_posts, f, ensure_ascii=False, indent=2)

        print(f"✓ Posts guardados en: {nombre_posts}")
        print(f"✓ Posts (latest) en: {ARCHIVO_POSTS_LATEST}")
        print("=" * 60)
        print("\nPosts listos. Pide a Claude Code que cree el borrador de email.")

        return {
            "informe": str(nombre_informe),
            "posts": str(nombre_posts),
            "datos_posts": datos_posts,
        }

    def get_latest_posts(self) -> dict:
        """Lee los últimos posts generados desde reports/posts_latest.json."""
        if not ARCHIVO_POSTS_LATEST.exists():
            return {}
        with open(ARCHIVO_POSTS_LATEST, encoding="utf-8") as f:
            return json.load(f)

    def search_and_summarize(self, query: str) -> str:
        """Realiza una búsqueda puntual y devuelve un resumen."""
        print(f"\n→ Buscando: '{query}'...")
        resultados = self.buscador.search(query, max_results=5)

        if not resultados:
            return "No se encontraron resultados para tu consulta."

        print(f"→ {len(resultados)} resultados encontrados. Resumiendo con IA...")
        return self.resumidor.summarize_search_results(query, resultados)
