"""
Generador de posts de LinkedIn sobre noticias de IA.
Genera 2 versiones con tópicos y enfoques distintos.
"""

import os
from typing import Optional
import anthropic

SYSTEM_PROMPT = """Eres un experto en comunicación digital y marketing de contenidos especializado en inteligencia artificial.
Tu misión es crear posts de LinkedIn que sean auténticos, informativos y que generen engagement.
Los posts deben sonar como escritos por un profesional del sector, no como marketing genérico.
Escribes siempre en español, con un tono cercano pero profesional."""

PLANTILLA_POST_1 = """A partir de este resumen de noticias sobre IA de la semana:

{resumen}

Genera un post de LinkedIn sobre EL AVANCE O NOTICIA MÁS IMPACTANTE de esta semana en IA.

El post debe:
- Empezar con un gancho potente (primera línea que pare el scroll)
- Tener entre 150-250 palabras
- Incluir 3-5 puntos clave con saltos de línea para facilitar la lectura
- Terminar con una pregunta o reflexión que invite a comentar
- Incluir 3-5 hashtags relevantes al final
- Sonar auténtico, no corporativo

Devuelve SOLO el texto del post, listo para copiar y pegar en LinkedIn."""

PLANTILLA_POST_2 = """A partir de este resumen de noticias sobre IA de la semana:

{resumen}

Genera un post de LinkedIn sobre UN TÓPICO DIFERENTE al más obvio: enfócate en las IMPLICACIONES PRÁCTICAS para profesionales, o en un avance que pase más desapercibido pero sea relevante, o en cómo estas noticias afectan a sectores concretos (salud, educación, trabajo, etc.).

El post debe:
- Empezar con un dato sorprendente o una pregunta provocadora
- Tener entre 150-250 palabras
- Usar un tono más reflexivo y analítico que el típico post de tecnología
- Aportar una perspectiva original o contrarian si la hay
- Terminar con una llamada a la acción concreta
- Incluir 3-5 hashtags relevantes al final

Devuelve SOLO el texto del post, listo para copiar y pegar en LinkedIn."""


class LinkedInGenerator:
    """Genera posts de LinkedIn a partir de resúmenes de noticias de IA."""

    MODEL = "claude-sonnet-4-6"
    MAX_TOKENS = 1024

    def __init__(self, api_key: Optional[str] = None):
        clave = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not clave:
            raise ValueError(
                "No se encontró ANTHROPIC_API_KEY. Configura el archivo .env"
            )
        self.client = anthropic.Anthropic(api_key=clave)

    def _generar_post(self, prompt: str) -> str:
        try:
            respuesta = self.client.messages.create(
                model=self.MODEL,
                max_tokens=self.MAX_TOKENS,
                system=[
                    {
                        "type": "text",
                        "text": SYSTEM_PROMPT,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
                messages=[{"role": "user", "content": prompt}],
            )
            return respuesta.content[0].text.strip()
        except anthropic.AuthenticationError:
            return "Error: API key inválida."
        except anthropic.RateLimitError:
            return "Error: Límite de tasa alcanzado. Intenta de nuevo en unos minutos."
        except anthropic.APIError as e:
            return f"Error de API: {e}"

    def generar_dos_posts(self, resumen_noticias: str) -> dict:
        """
        Genera 2 posts de LinkedIn con enfoques distintos.

        Args:
            resumen_noticias: Texto del informe semanal de noticias IA.

        Returns:
            Dict con 'post_1' (noticia más impactante) y 'post_2' (tópico alternativo).
        """
        print("\n→ Generando post LinkedIn #1 (noticia más impactante)...")
        post_1 = self._generar_post(PLANTILLA_POST_1.format(resumen=resumen_noticias[:3000]))

        print("→ Generando post LinkedIn #2 (perspectiva alternativa)...")
        post_2 = self._generar_post(PLANTILLA_POST_2.format(resumen=resumen_noticias[:3000]))

        return {"post_1": post_1, "post_2": post_2}
