"""
Utilidad para extraer texto limpio de una URL.
Usado por Claude Code para leer el contenido de páginas de noticias.
"""

import sys
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def fetch_text(url: str, max_chars: int = 3000) -> str:
    """Descarga una URL y devuelve su texto limpio."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=10, verify=False)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()
        return " ".join(soup.get_text(separator=" ", strip=True).split())[:max_chars]
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python search_connector.py <url>")
        sys.exit(1)
    print(fetch_text(sys.argv[1]))
