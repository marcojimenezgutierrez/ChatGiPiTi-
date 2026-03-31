"""
config.py — Carga y validación de la configuración de la aplicación.

Lee la API key de Gemini desde una variable de entorno o desde un archivo .env.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Nombre exacto de la variable de entorno que se debe definir
_ENV_VAR = "GEMINI_API_KEY"

# Modelo de Gemini a utilizar
GEMINI_MODEL = "gemini-1.5-flash"

# Nombre que mostrará el asistente en la consola
ASSISTANT_NAME = "ChatGiPiTi"

# Prompt de sistema: define la personalidad del asistente
SYSTEM_PROMPT = (
    "Eres un amigo cercano, amable y de confianza. "
    "Siempre hablas en español de forma natural y conversacional. "
    "Tus respuestas son cálidas, humanas y empáticas, pero concisas: "
    "no escribas párrafos interminables, ve al punto con simpatía. "
    "Si no sabes algo, lo reconoces con honestidad. "
    "Nunca inventas información ni das consejos peligrosos. "
    "Evitas sonar robótico o demasiado formal. "
    "Usas un tono positivo y cercano, como si chatearas con un buen amigo."
)


def cargar_configuracion() -> str:
    """
    Carga la API key de Gemini desde el entorno o desde un archivo .env.

    Busca el archivo .env en la raíz del proyecto (directorio padre de src/).

    Returns:
        str: La API key lista para usar.

    Raises:
        EnvironmentError: Si la variable de entorno no está definida o está vacía.
    """
    # Intentar cargar desde un archivo .env ubicado en la raíz del proyecto
    ruta_env = Path(__file__).parent.parent / ".env"
    load_dotenv(dotenv_path=ruta_env)

    api_key = os.getenv(_ENV_VAR, "").strip()

    if not api_key:
        raise EnvironmentError(
            f"\n❌  No se encontró la variable de entorno '{_ENV_VAR}'.\n"
            "   Crea un archivo .env en la raíz del proyecto con el contenido:\n"
            f"   {_ENV_VAR}=tu_api_key_aqui\n"
            "   Puedes basarte en el archivo .env.example incluido.\n"
            "   Obtén tu API key gratuita en: https://aistudio.google.com/app/apikey\n"
        )

    return api_key
