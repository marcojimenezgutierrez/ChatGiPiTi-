"""
app.py — Punto de entrada de ChatGiPiTi.

Ejecuta la aplicación de chat con Gemini API desde la consola.

Uso:
    python app.py
"""

import sys

from src.chatbot import ChatBot
from src.config import cargar_configuracion
from src.ui import ejecutar_chat


def main() -> None:
    """Carga la configuración, crea el chatbot y lanza la interfaz de consola."""
    try:
        api_key = cargar_configuracion()
    except EnvironmentError as error:
        print(error)
        sys.exit(1)

    try:
        bot = ChatBot(api_key=api_key)
    except Exception as error:  # noqa: BLE001
        print(f"\n❌  No se pudo inicializar el chatbot: {error}\n")
        sys.exit(1)

    ejecutar_chat(bot)


if __name__ == "__main__":
    main()
