"""
Módulo de búsqueda web usando DuckDuckGo sin API key.
Extrae contenido limpio de páginas web con BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from typing import Optional


class ChromeSearchConnector:
    """Conector de búsqueda web usando DuckDuckGo."""

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    REQUEST_TIMEOUT = 10
    MAX_CONTENT_CHARS = 2000

    def search(self, query: str, max_results: int = 5) -> list[dict]:
        """
        Realiza una búsqueda en DuckDuckGo.

        Args:
            query: Consulta de búsqueda.
            max_results: Número máximo de resultados a devolver.

        Returns:
            Lista de dicts con claves 'title', 'url' y 'snippet'.
        """
        resultados = []
        try:
            with DDGS() as ddgs:
                for r in ddgs.text(query, max_results=max_results):
                    resultados.append(
                        {
                            "title": r.get("title", "Sin título"),
                            "url": r.get("href", ""),
                            "snippet": r.get("body", "Sin descripción"),
                        }
                    )
        except Exception as e:
            print(f"  [!] Error al buscar '{query}': {e}")
        return resultados

    def fetch_page_content(self, url: str) -> Optional[str]:
        """
        Descarga y extrae texto limpio de una página web.

        Args:
            url: URL de la página a descargar.

        Returns:
            Texto limpio de la página (máx 2000 caracteres) o None si falla.
        """
        try:
            response = requests.get(
                url,
                headers=self.HEADERS,
                timeout=self.REQUEST_TIMEOUT,
                verify=False,
            )
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Eliminar scripts, estilos y elementos no deseados
            for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
                tag.decompose()

            texto = soup.get_text(separator=" ", strip=True)
            # Normalizar espacios en blanco
            texto = " ".join(texto.split())
            return texto[: self.MAX_CONTENT_CHARS]

        except requests.exceptions.SSLError:
            # Reintento sin verificación SSL ya incluido arriba (verify=False)
            pass
        except requests.exceptions.Timeout:
            print(f"  [!] Timeout al acceder a: {url}")
        except requests.exceptions.TooManyRedirects:
            print(f"  [!] Demasiadas redirecciones: {url}")
        except requests.exceptions.RequestException as e:
            print(f"  [!] Error al descargar {url}: {e}")
        except Exception as e:
            print(f"  [!] Error inesperado procesando {url}: {e}")
        return None
