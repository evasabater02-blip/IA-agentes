"""
CLI principal del conector de búsqueda + agente de noticias IA.

Uso (desde la carpeta routines/):
    python main.py search "tu consulta"   → busca y resume
    python main.py news                   → genera informe semanal + posts LinkedIn
    python main.py posts                  → muestra los últimos posts generados
    python main.py schedule               → modo automático semanal (lunes 08:00)
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Asegurar que el directorio del script está en el path para imports locales
sys.path.insert(0, str(Path(__file__).parent))

# Cargar variables de entorno desde .env si existe (busca en routines/ y en la raíz)
try:
    from dotenv import load_dotenv
    env_local = Path(__file__).parent / ".env"
    env_root = Path(__file__).parent.parent / ".env"
    if env_local.exists():
        load_dotenv(env_local)
    elif env_root.exists():
        load_dotenv(env_root)
except ImportError:
    pass


def cmd_search(query: str):
    from news_agent import AINewsAgent
    agente = AINewsAgent()
    resultado = agente.search_and_summarize(query)
    print("\n" + "=" * 60)
    print("RESUMEN:")
    print("=" * 60)
    print(resultado)


def cmd_news():
    from news_agent import AINewsAgent
    agente = AINewsAgent()
    resultado = agente.run_weekly_report()
    if resultado:
        print(f"\nInforme: {resultado.get('informe', '')}")
        print(f"Posts:   {resultado.get('posts', '')}")
        print("\nPide a Claude Code: 'crea el borrador de email con los últimos posts'")


def cmd_posts():
    from news_agent import AINewsAgent
    agente = AINewsAgent()
    datos = agente.get_latest_posts()

    if not datos:
        print("No hay posts generados todavía. Ejecuta primero: python main.py news")
        return

    print(f"\n{'=' * 60}")
    print(f"Posts generados el {datos.get('generado_el', '?')} | Semana {datos.get('semana', '?')}")
    print(f"{'=' * 60}")
    print(f"\n--- POST #1: {datos['post_1']['titulo']} ---\n")
    print(datos["post_1"]["contenido"])
    print(f"\n--- POST #2: {datos['post_2']['titulo']} ---\n")
    print(datos["post_2"]["contenido"])


def cmd_schedule():
    try:
        import schedule
        import time
        from datetime import datetime
    except ImportError:
        print("Error: instala 'schedule' con: pip install schedule")
        sys.exit(1)

    from news_agent import AINewsAgent

    def ejecutar_informe():
        print(f"\n[{datetime.now().strftime('%d/%m/%Y %H:%M')}] Ejecutando informe semanal...")
        agente = AINewsAgent()
        agente.run_weekly_report()

    schedule.every().monday.at("08:00").do(ejecutar_informe)

    proxima = schedule.next_run()
    print("Modo automático semanal activado (cada lunes a las 08:00).")
    print(f"Próxima ejecución: {proxima.strftime('%d/%m/%Y a las %H:%M')}")
    print("Presiona Ctrl+C para detener.\n")

    while True:
        schedule.run_pending()
        time.sleep(60)


def main():
    parser = argparse.ArgumentParser(
        description="Agente semanal de noticias IA + generador de posts LinkedIn",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python main.py search "últimas noticias sobre GPT-5"
  python main.py news
  python main.py posts
  python main.py schedule

Cron semanal (cada lunes 08:00):
  0 8 * * 1 cd /ruta/routines && /ruta/.venv/bin/python main.py news
        """,
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    p_search = subparsers.add_parser("search", help="Busca y resume una consulta")
    p_search.add_argument("query", help="Consulta de búsqueda")

    subparsers.add_parser("news", help="Genera informe semanal + 2 posts LinkedIn")
    subparsers.add_parser("posts", help="Muestra los últimos posts de LinkedIn generados")
    subparsers.add_parser("schedule", help="Activa el modo automático (lunes 08:00)")

    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: No se encontró ANTHROPIC_API_KEY.")
        print("Edita routines/.env (o .env en la raíz) y añade tu clave de Anthropic")
        sys.exit(1)

    if args.comando == "search":
        cmd_search(args.query)
    elif args.comando == "news":
        cmd_news()
    elif args.comando == "posts":
        cmd_posts()
    elif args.comando == "schedule":
        cmd_schedule()


if __name__ == "__main__":
    main()
