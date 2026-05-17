"""
CLI principal del conector de búsqueda + agente de noticias IA.

Uso:
    python main.py search "tu consulta"   → busca y resume
    python main.py news                   → genera informe mensual
    python main.py schedule               → modo automático (día 1 de cada mes)
"""

import argparse
import os
import sys
from pathlib import Path

# Cargar variables de entorno desde .env si existe
try:
    from dotenv import load_dotenv
    load_dotenv()
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
    ruta = agente.run_monthly_report()
    if ruta:
        print(f"\nInforme disponible en: {ruta}")


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
        print(f"\n[{datetime.now().strftime('%d/%m/%Y %H:%M')}] Ejecutando informe mensual...")
        agente = AINewsAgent()
        agente.run_monthly_report()

    # Ejecutar el día 1 de cada mes a las 8:00
    schedule.every().month.at("08:00").do(ejecutar_informe)

    proxima = schedule.next_run()
    print(f"Modo automático activado.")
    print(f"Próxima ejecución: {proxima.strftime('%d/%m/%Y a las %H:%M')}")
    print("Presiona Ctrl+C para detener.\n")

    while True:
        schedule.run_pending()
        time.sleep(60)


def main():
    parser = argparse.ArgumentParser(
        description="Conector de búsqueda web + agente de noticias IA",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python main.py search "últimas noticias sobre ChatGPT"
  python main.py news
  python main.py schedule
        """,
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    # Subcomando: search
    p_search = subparsers.add_parser("search", help="Busca y resume una consulta")
    p_search.add_argument("query", help="Consulta de búsqueda")

    # Subcomando: news
    subparsers.add_parser("news", help="Genera informe mensual de noticias de IA")

    # Subcomando: schedule
    subparsers.add_parser("schedule", help="Activa el modo automático mensual")

    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: No se encontró ANTHROPIC_API_KEY.")
        print("1. Copia .env.example a .env")
        print("2. Edita .env y añade tu clave de Anthropic")
        sys.exit(1)

    if args.comando == "search":
        cmd_search(args.query)
    elif args.comando == "news":
        cmd_news()
    elif args.comando == "schedule":
        cmd_schedule()


if __name__ == "__main__":
    main()
