#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROUTINES_DIR="$SCRIPT_DIR/routines"

echo "======================================"
echo "  Instalando Agente Semanal de IA"
echo "======================================"

# Verificar Python 3.8+
if ! command -v python3 &>/dev/null; then
    echo "Error: Python 3 no encontrado. Instálalo desde https://python.org"
    exit 1
fi

PYTHON_VERSION=$(python3 -c "import sys; print(sys.version_info.minor)")
if [ "$PYTHON_VERSION" -lt 8 ]; then
    echo "Error: Se requiere Python 3.8 o superior"
    exit 1
fi

echo "✓ Python $(python3 --version) detectado"

# Crear entorno virtual en la raíz del proyecto
if [ ! -d "$SCRIPT_DIR/.venv" ]; then
    echo "→ Creando entorno virtual..."
    python3 -m venv "$SCRIPT_DIR/.venv"
    echo "✓ Entorno virtual creado en .venv/"
else
    echo "✓ Entorno virtual ya existe"
fi

# Instalar dependencias desde routines/requirements.txt
echo "→ Instalando dependencias..."
"$SCRIPT_DIR/.venv/bin/pip" install --quiet --upgrade pip
"$SCRIPT_DIR/.venv/bin/pip" install --quiet -r "$ROUTINES_DIR/requirements.txt"
echo "✓ Dependencias instaladas"

# Copiar .env si no existe (en routines/)
if [ ! -f "$ROUTINES_DIR/.env" ]; then
    cp "$ROUTINES_DIR/.env.example" "$ROUTINES_DIR/.env"
    echo "✓ Archivo routines/.env creado (edítalo con tu API key)"
else
    echo "✓ Archivo routines/.env ya existe"
fi

# Crear directorio de informes
mkdir -p "$ROUTINES_DIR/reports"
echo "✓ Directorio routines/reports/ listo"

echo ""
echo "======================================"
echo "  Instalación completada"
echo "======================================"
echo ""
echo "PRÓXIMOS PASOS:"
echo ""
echo "1. Añade tu ANTHROPIC_API_KEY en routines/.env:"
echo "   nano routines/.env"
echo ""
echo "2. Activa el entorno virtual:"
echo "   source .venv/bin/activate"
echo ""
echo "3. Prueba una búsqueda:"
echo "   cd routines && python main.py search \"noticias IA 2026\""
echo ""
echo "4. Genera el informe semanal + posts LinkedIn:"
echo "   cd routines && python main.py news"
echo ""
echo "Cron automático (cada lunes 08:00):"
echo "   0 8 * * 1 cd $ROUTINES_DIR && $SCRIPT_DIR/.venv/bin/python main.py news"
echo ""
