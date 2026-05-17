"""
Módulo de resumen con IA usando la API de Anthropic (Claude).
Implementa prompt caching para reducir costes en llamadas repetidas.
"""

import os
from datetime import datetime
from typing import Optional

import anthropic


SYSTEM_PROMPT_BUSQUEDA = """Eres un asistente experto en inteligencia artificial y tecnología.
Tu tarea es analizar resultados de búsqueda web y generar resúmenes claros y útiles en español.
Cuando recibas resultados de búsqueda, sintetiza la información más relevante de forma concisa y precisa.
Responde siempre en español, con un tono profesional pero accesible."""

SYSTEM_PROMPT_NOTICIAS = """Eres un analista experto en inteligencia artificial y tecnología de vanguardia.
Tu especialidad es generar informes mensuales estructurados sobre los avances más importantes en IA.
Debes sintetizar múltiples fuentes de información en un informe coherente, bien organizado y en español.
El informe debe ser profesional, informativo y útil para lectores con conocimientos técnicos medios."""


class AISummarizer:
    """Resumidor de contenido usando Claude (claude-sonnet-4-6)."""

    MODEL = "claude-sonnet-4-6"
    MAX_TOKENS = 4096

    def __init__(self, api_key: Optional[str] = None):
        """
        Inicializa el cliente de Anthropic.

        Args:
            api_key: Clave de API. Si no se proporciona, se lee de ANTHROPIC_API_KEY.

        Raises:
            ValueError: Si no se encuentra la clave de API.
        """
        clave = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not clave:
            raise ValueError(
                "No se encontró ANTHROPIC_API_KEY. "
                "Por favor, configura la variable de entorno o el archivo .env"
            )
        self.client = anthropic.Anthropic(api_key=clave)

    def summarize_search_results(self, query: str, results: list[dict]) -> str:
        """
        Resume los resultados de búsqueda usando Claude.

        Utiliza cache_control en el prompt del sistema para aprovechar
        el prompt caching de Anthropic y reducir costes.

        Args:
            query: Consulta original de búsqueda.
            results: Lista de resultados con 'title', 'url' y 'snippet'.

        Returns:
            Resumen en español de los resultados.
        """
        if not results:
            return "No se encontraron resultados para esta búsqueda."

        # Formatear los resultados para el prompt
        resultados_texto = "\n\n".join(
            f"**{i+1}. {r['title']}**\n"
            f"URL: {r['url']}\n"
            f"Descripción: {r['snippet']}"
            for i, r in enumerate(results)
        )

        prompt_usuario = (
            f"Consulta de búsqueda: '{query}'\n\n"
            f"Resultados encontrados:\n\n{resultados_texto}\n\n"
            "Por favor, proporciona un resumen claro y útil de estos resultados en español. "
            "Destaca los puntos más importantes y relevantes para la consulta."
        )

        try:
            respuesta = self.client.messages.create(
                model=self.MODEL,
                max_tokens=self.MAX_TOKENS,
                system=[
                    {
                        "type": "text",
                        "text": SYSTEM_PROMPT_BUSQUEDA,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
                messages=[{"role": "user", "content": prompt_usuario}],
            )
            return respuesta.content[0].text
        except anthropic.AuthenticationError:
            return "Error: API key inválida. Verifica tu configuración."
        except anthropic.RateLimitError:
            return "Error: Límite de tasa alcanzado. Intenta de nuevo en unos minutos."
        except anthropic.APIError as e:
            return f"Error de API: {e}"

    def summarize_news_batch(self, articles: list[dict]) -> str:
        """
        Genera un informe mensual estructurado a partir de múltiples artículos de noticias.

        Usa cache_control en el prompt del sistema para prompt caching.

        Args:
            articles: Lista de artículos con 'title', 'url' y 'snippet'.

        Returns:
            Informe mensual en Markdown con todas las noticias y conclusión.
        """
        if not articles:
            return "# Informe Mensual de IA\n\nNo se encontraron noticias para este período."

        fecha_actual = datetime.now().strftime("%B %Y")
        mes_anio = datetime.now().strftime("%Y-%m")

        # Formatear artículos para el prompt
        articulos_texto = "\n\n".join(
            f"ARTÍCULO {i+1}:\n"
            f"Título: {a['title']}\n"
            f"Fuente: {a['url']}\n"
            f"Contenido: {a['snippet']}"
            for i, a in enumerate(articles)
        )

        prompt_informe = (
            f"Fecha del informe: {fecha_actual}\n\n"
            f"A continuación tienes {len(articles)} artículos y resultados de búsqueda "
            f"sobre inteligencia artificial del último mes:\n\n"
            f"{articulos_texto}\n\n"
            "Genera un informe mensual completo en formato Markdown con la siguiente estructura:\n\n"
            "1. **Título del informe** con fecha\n"
            "2. **Resumen ejecutivo** (2-3 párrafos generales)\n"
            "3. **Noticias destacadas**: Para cada noticia relevante:\n"
            "   - ### Título de la noticia\n"
            "   - **Fecha aproximada**: (si se puede deducir del contexto)\n"
            "   - Resumen de 2-3 líneas explicando la noticia\n"
            "   - **Fuente**: URL\n"
            "4. **Conclusiones y tendencias**: Un párrafo final sobre las tendencias "
            "principales del mes en IA\n\n"
            "El informe debe estar completamente en español y ser informativo y profesional."
        )

        try:
            respuesta = self.client.messages.create(
                model=self.MODEL,
                max_tokens=self.MAX_TOKENS,
                system=[
                    {
                        "type": "text",
                        "text": SYSTEM_PROMPT_NOTICIAS,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
                messages=[{"role": "user", "content": prompt_informe}],
            )
            return respuesta.content[0].text
        except anthropic.AuthenticationError:
            return "Error: API key inválida. Verifica tu configuración."
        except anthropic.RateLimitError:
            return "Error: Límite de tasa alcanzado. Intenta de nuevo en unos minutos."
        except anthropic.APIError as e:
            return f"Error de API al generar informe: {e}"
