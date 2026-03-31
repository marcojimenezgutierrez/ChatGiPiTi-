"""
chatbot.py — Lógica principal del chatbot con Gemini API.

Gestiona la sesión de chat, el historial conversacional y la comunicación
con el modelo de lenguaje de Google Gemini.
"""

from google import genai
from google.genai import errors as genai_errors
from google.genai import types

from .config import GEMINI_MODEL, SYSTEM_PROMPT


class ChatBot:
    """
    Encapsula una sesión de chat continua con Gemini.

    Mantiene el historial de la conversación en memoria durante la sesión,
    lo que permite que el modelo recuerde el contexto previo.
    """

    def __init__(self, api_key: str) -> None:
        """
        Inicializa el cliente de Gemini y arranca una sesión de chat.

        Args:
            api_key: La API key de Google AI obtenida desde la configuración.
        """
        self._client = genai.Client(api_key=api_key)

        # Configuración del modelo con el prompt de sistema
        self._config = types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
        )

        # Sesión de chat con historial automático gestionado por el SDK
        self._sesion = self._client.chats.create(
            model=GEMINI_MODEL,
            config=self._config,
        )

    # ------------------------------------------------------------------
    # Interfaz pública
    # ------------------------------------------------------------------

    def enviar_mensaje(self, texto: str) -> str:
        """
        Envía un mensaje al modelo y devuelve la respuesta como texto.

        Args:
            texto: El mensaje escrito por el usuario.

        Returns:
            str: La respuesta generada por el asistente.

        Raises:
            ConnectionError: Si hay problemas de red o el servicio no responde.
            PermissionError: Si la API key es inválida o la cuota está agotada.
            RuntimeError: Para cualquier otro error de la API.
        """
        try:
            respuesta = self._sesion.send_message(texto)
            return respuesta.text

        except genai_errors.ClientError as error:
            # Errores 4xx: autenticación, cuota, petición inválida, etc.
            codigo = getattr(error, "code", 0)
            if codigo == 401 or codigo == 403:
                raise PermissionError(
                    "❌  API key inválida o sin permisos. "
                    "Verifica que tu GEMINI_API_KEY sea correcta."
                )
            if codigo == 429:
                raise PermissionError(
                    "❌  Cuota de la API agotada. "
                    "Espera unos minutos o revisa tu plan en Google AI Studio."
                )
            raise RuntimeError(f"❌  Error del cliente ({codigo}): {error}")

        except genai_errors.ServerError as error:
            raise ConnectionError(
                f"❌  El servicio de Gemini no está disponible en este momento "
                f"({getattr(error, 'code', '')}). "
                "Comprueba tu conexión a Internet e inténtalo de nuevo."
            )

        except Exception as error:
            raise RuntimeError(f"❌  Error inesperado al contactar con Gemini: {error}")

    def limpiar_historial(self) -> None:
        """
        Reinicia el historial de la conversación iniciando una nueva sesión.

        El modelo ya no recordará los mensajes anteriores.
        """
        self._sesion = self._client.chats.create(
            model=GEMINI_MODEL,
            config=self._config,
        )

    @property
    def num_mensajes(self) -> int:
        """Devuelve el número de turnos en el historial de la sesión actual."""
        return len(self._sesion.get_history())
