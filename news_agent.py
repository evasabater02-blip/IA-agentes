"""
Agente principal que orquesta búsqueda web + resumen con IA.
Genera informes mensuales sobre noticias de inteligencia artificial.
"""

import os
from datetime import datetime
from pathlib import Path

from search_connector import ChromeSearchConnector
from ai_summarizer import AISummarizer


# Queries para el informe mensual de noticias de IA
QUERIES_NOTICIAS_IA = [
    "inteligencia artificial noticias",
    "AI news this month",
    "machine learning avances",
    "LLM nuevos modelos",
    "IA empresas tecnología",
]

DIRECTORIO_INFORMES = Path("reports")


class AINewsAgent:
    """Agente que busca noticias de IA y genera informes mensuales."""

    def __init__(self):
        self.buscador = ChromeSearchConnector()
        self.resumidor = AISummarizer()
        DIRECTORIO_INFORMES.mkdir(exist_ok=True)

    def run_monthly_report(self) -> str:
        """
        Ejecuta el flujo completo para generar el informe mensual de noticias de IA.

        1. Busca con múltiples queries sobre noticias de IA del último mes.
        2. Deduplica resultados por URL.
        3. Genera resumen con AISummarizer.
        4. Guarda el informe en reports/informe_IA_YYYY-MM.md.
        5. Retorna la ruta del archivo guardado.

        Returns:
            Ruta absoluta del informe generado.
        """
        print("\n" + "=" * 60)
        print("   GENERANDO INFORME MENSUAL DE NOTICIAS IA")
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
            return ""

        print("\n→ Generando informe con Claude (esto puede tardar unos segundos)...")
        informe = self.resumidor.summarize_news_batch(todos_los_resultados)

        # Determinar nombre de archivo
        mes_anio = datetime.now().strftime("%Y-%m")
        nombre_archivo = DIRECTORIO_INFORMES / f"informe_IA_{mes_anio}.md"

        # Encabezado con metadatos
        encabezado = (
            f"<!-- Informe generado automáticamente el "
            f"{datetime.now().strftime('%d/%m/%Y a las %H:%M')} -->\n"
            f"<!-- Fuentes consultadas: {len(todos_los_resultados)} resultados únicos -->\n\n"
        )

        contenido_final = encabezado + informe

        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(contenido_final)

        ruta_absoluta = str(nombre_archivo.resolve())
        print(f"\n✓ Informe guardado en: {ruta_absoluta}")
        print("=" * 60)
        return ruta_absoluta

    def search_and_summarize(self, query: str) -> str:
        """
        Realiza una búsqueda puntual y devuelve un resumen del resultado.

        Args:
            query: Consulta de búsqueda del usuario.

        Returns:
            Resumen en español de los resultados encontrados.
        """
        print(f"\n→ Buscando: '{query}'...")
        resultados = self.buscador.search(query, max_results=5)

        if not resultados:
            return "No se encontraron resultados para tu consulta."

        print(f"→ {len(resultados)} resultados encontrados. Resumiendo con IA...")
        resumen = self.resumidor.summarize_search_results(query, resultados)
        return resumen
