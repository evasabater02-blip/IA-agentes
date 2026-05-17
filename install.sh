#!/bin/bash
set -e

echo "======================================"
echo "  Instalando Conector de Búsqueda IA"
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

# Crear entorno virtual
if [ ! -d ".venv" ]; then
    echo "→ Creando entorno virtual..."
    python3 -m venv .venv
    echo "✓ Entorno virtual creado en .venv/"
else
    echo "✓ Entorno virtual ya existe"
fi

# Activar entorno e instalar dependencias
echo "→ Instalando dependencias..."
.venv/bin/pip install --quiet --upgrade pip
.venv/bin/pip install --quiet -r requirements.txt
echo "✓ Dependencias instaladas"

# Copiar .env si no existe
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✓ Archivo .env creado (edítalo con tu API key)"
else
    echo "✓ Archivo .env ya existe"
fi

# Crear directorio de informes
mkdir -p reports
echo "✓ Directorio reports/ listo"

echo ""
echo "======================================"
echo "  Instalación completada"
echo "======================================"
echo ""
echo "PRÓXIMOS PASOS:"
echo ""
echo "1. Edita .env y añade tu ANTHROPIC_API_KEY:"
echo "   nano .env"
echo ""
echo "2. Activa el entorno virtual:"
echo "   source .venv/bin/activate"
echo ""
echo "3. Prueba una búsqueda:"
echo "   python main.py search \"noticias IA 2026\""
echo ""
echo "4. Genera un informe mensual:"
echo "   python main.py news"
echo ""
echo "Para cron automático mensual, añade a crontab:"
echo "   0 8 1 * * cd $(pwd) && .venv/bin/python main.py news"
echo ""
