"""
ui.py — Interfaz de usuario para la consola.

Gestiona la presentación de mensajes, el bucle principal de chat
y los comandos especiales del usuario.
"""

from .chatbot import ChatBot
from .config import ASSISTANT_NAME

# ──────────────────────────────────────────────
# Colores ANSI para hacer la consola más amigable
# ──────────────────────────────────────────────
_RESET = "\033[0m"
_NEGRITA = "\033[1m"
_CYAN = "\033[96m"
_VERDE = "\033[92m"
_AMARILLO = "\033[93m"
_ROJO = "\033[91m"
_GRIS = "\033[90m"

_COMANDOS = {
    "/salir": "Termina la sesión de chat.",
    "/limpiar": "Borra el historial de la conversación actual.",
    "/ayuda": "Muestra esta lista de comandos.",
}


def _imprimir_bienvenida() -> None:
    """Muestra el mensaje de bienvenida al iniciar la aplicación."""
    linea = "─" * 50
    print(f"\n{_CYAN}{_NEGRITA}{linea}{_RESET}")
    print(f"{_CYAN}{_NEGRITA}  👋  ¡Hola! Soy {ASSISTANT_NAME}, tu asistente amigo.{_RESET}")
    print(f"{_GRIS}  Escribe un mensaje para empezar a chatear.{_RESET}")
    print(f"{_GRIS}  Escribe {_AMARILLO}/ayuda{_GRIS} para ver los comandos disponibles.{_RESET}")
    print(f"{_CYAN}{_NEGRITA}{linea}{_RESET}\n")


def _imprimir_ayuda() -> None:
    """Muestra la lista de comandos disponibles."""
    print(f"\n{_AMARILLO}{_NEGRITA}📋  Comandos disponibles:{_RESET}")
    for cmd, desc in _COMANDOS.items():
        print(f"  {_AMARILLO}{cmd:<12}{_RESET} {desc}")
    print()


def _imprimir_respuesta(texto: str) -> None:
    """Imprime la respuesta del asistente con formato."""
    print(f"\n{_VERDE}{_NEGRITA}{ASSISTANT_NAME}:{_RESET}")
    print(f"  {texto.strip()}\n")


def _imprimir_error(mensaje: str) -> None:
    """Imprime un mensaje de error."""
    print(f"\n{_ROJO}{mensaje}{_RESET}\n")


def _imprimir_info(mensaje: str) -> None:
    """Imprime un mensaje informativo."""
    print(f"\n{_AMARILLO}ℹ️  {mensaje}{_RESET}\n")


def ejecutar_chat(bot: ChatBot) -> None:
    """
    Bucle principal de la interfaz de chat en consola.

    Lee la entrada del usuario, gestiona los comandos especiales
    y muestra las respuestas del asistente hasta que el usuario
    escriba '/salir' o presione Ctrl+C / Ctrl+D.

    Args:
        bot: Instancia de ChatBot ya inicializada y lista para usarse.
    """
    _imprimir_bienvenida()

    while True:
        try:
            entrada = input(f"{_CYAN}{_NEGRITA}Tú:{_RESET} ").strip()
        except (KeyboardInterrupt, EOFError):
            # El usuario presionó Ctrl+C o Ctrl+D
            print()
            _imprimir_info("Sesión finalizada. ¡Hasta pronto! 👋")
            break

        # ── Comando: salir ────────────────────────────────────────────
        if entrada.lower() == "/salir":
            _imprimir_info("Sesión finalizada. ¡Hasta pronto! 👋")
            break

        # ── Comando: ayuda ────────────────────────────────────────────
        if entrada.lower() == "/ayuda":
            _imprimir_ayuda()
            continue

        # ── Comando: limpiar ──────────────────────────────────────────
        if entrada.lower() == "/limpiar":
            bot.limpiar_historial()
            _imprimir_info("Historial borrado. ¡Empecemos de nuevo! 🧹")
            continue

        # ── Entrada vacía ─────────────────────────────────────────────
        if not entrada:
            _imprimir_error("Por favor escribe algo. Aquí estoy para escucharte 😊")
            continue

        # ── Enviar mensaje al modelo ──────────────────────────────────
        try:
            respuesta = bot.enviar_mensaje(entrada)
            _imprimir_respuesta(respuesta)
        except (PermissionError, ConnectionError, RuntimeError) as error:
            _imprimir_error(str(error))
