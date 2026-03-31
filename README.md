# ChatGiPiTi 🤖💬

> **Tu asistente-amigo en la consola, impulsado por Google Gemini.**

ChatGiPiTi es una aplicación de chat en Python que se ejecuta en la terminal y usa la **Gemini API** de Google para generar respuestas naturales, cálidas y conversacionales — como si chatearas con un buen amigo.

---

## 📐 Arquitectura del proyecto

```
ChatGiPiTi-/
├── app.py              ← Punto de entrada; inicializa config, bot y UI
├── requirements.txt    ← Dependencias del proyecto
├── .env.example        ← Plantilla del archivo de entorno (sin secretos)
├── .gitignore          ← Excluye .env, __pycache__, venv, etc.
├── README.md           ← Esta documentación
└── src/
    ├── __init__.py     ← Marca src/ como paquete Python
    ├── config.py       ← Lee la API key y define ajustes globales
    ├── chatbot.py      ← Gestiona la sesión Gemini y el historial
    └── ui.py           ← Interfaz de consola: bucle de chat y comandos
```

### Flujo de datos

```
Usuario (teclado)
       │
       ▼
    ui.py  ──────────────────────────────► chatbot.py
    (lee entrada, valida, llama a bot)      (envía a Gemini API, devuelve texto)
       │                                           │
       ▼                                           │
  Muestra respuesta ◄────────────────────────────┘
```

- **`config.py`** se ejecuta al arrancar y carga `GEMINI_API_KEY` desde `.env` o el entorno del sistema.
- **`chatbot.py`** mantiene el historial en memoria durante la sesión (conversación continua).
- **`ui.py`** gestiona la presentación con colores ANSI y los comandos especiales.
- **`app.py`** orquesta todo: carga config → crea bot → lanza UI.

---

## 🚀 Guía de instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/marcojimenezgutierrez/ChatGiPiTi-.git
cd ChatGiPiTi-
```

### 2. Crear y activar un entorno virtual

```bash
# Crear el entorno virtual
python -m venv venv

# Activar en Linux / macOS
source venv/bin/activate

# Activar en Windows (PowerShell)
venv\Scripts\Activate.ps1

# Activar en Windows (cmd)
venv\Scripts\activate.bat
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la API key

1. Obtén tu API key gratuita en [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Copia el archivo de ejemplo:
   ```bash
   cp .env.example .env
   ```
3. Abre `.env` en tu editor y reemplaza el valor:
   ```
   GEMINI_API_KEY=AIzaSy...tu_api_key_real...
   ```

### 5. Ejecutar el proyecto

```bash
python app.py
```

---

## 💬 Comandos disponibles en el chat

| Comando    | Descripción                                      |
|------------|--------------------------------------------------|
| `/ayuda`   | Muestra la lista de comandos disponibles         |
| `/limpiar` | Borra el historial de la conversación actual     |
| `/salir`   | Termina la sesión (también funciona Ctrl+C)      |

---

## 🖥️ Ejemplo de conversación en consola

```
──────────────────────────────────────────────────
  👋  ¡Hola! Soy ChatGiPiTi, tu asistente amigo.
  Escribe un mensaje para empezar a chatear.
  Escribe /ayuda para ver los comandos disponibles.
──────────────────────────────────────────────────

Tú: hola, ¿cómo estás?

ChatGiPiTi:
  ¡Hola! Aquí andamos, bien y a tus órdenes 😄
  ¿Cómo estás tú? ¿En qué te puedo ayudar hoy?

Tú: explícame qué es una API en pocas palabras

ChatGiPiTi:
  ¡Claro! Una API es como un camarero en un restaurante:
  tú (el cliente) le pides algo, él va a la cocina (el servidor)
  y te trae lo que pediste. La API es ese intermediario que
  conecta tu aplicación con otro servicio de forma ordenada. 🍽️

Tú: /limpiar

ℹ️  Historial borrado. ¡Empecemos de nuevo! 🧹

Tú: /salir

ℹ️  Sesión finalizada. ¡Hasta pronto! 👋
```

---

## 🔒 Seguridad

### ⚠️ Nunca subas tu API key a Git

Tu API key es una credencial privada. Si la expones en un repositorio público:

- Terceros podrían usarla y agotar tu cuota.
- Google puede revocarla automáticamente al detectarla.

### ✅ Buenas prácticas incluidas en este proyecto

1. **`.env` está en `.gitignore`** — el archivo con tu clave real nunca se sube.
2. **`.env.example` SÍ se sube** — sirve de plantilla sin exponer secretos.
3. **`config.py` lee la clave en tiempo de ejecución** — no hay valores hardcodeados en el código.

### 🔍 Antes de hacer un commit, verifica

```bash
# Comprueba que .env no aparece en los archivos a confirmar
git status

# Si .env aparece por error, retíralo con:
git rm --cached .env
```

---

## 🛠️ Requisitos del sistema

- **Python 3.11 o superior**
- Conexión a Internet (para llamadas a la Gemini API)
- API key de [Google AI Studio](https://aistudio.google.com/app/apikey) (gratuita)

---

## 📦 Dependencias

| Paquete              | Versión mínima | Uso                                   |
|----------------------|---------------|---------------------------------------|
| `google-genai`       | 1.69.0        | Cliente oficial de Gemini API         |
| `python-dotenv`      | 1.2.2         | Carga variables desde el archivo .env |

---

## 🌱 Inicializar Git y hacer el primer commit

Si clonas este proyecto y quieres sincronizar tu propio repositorio:

```bash
# 1. Inicializar un repositorio nuevo (si es un proyecto vacío)
git init

# 2. Agregar todos los archivos (sin .env gracias al .gitignore)
git add .

# 3. Crear el primer commit
git commit -m "feat: proyecto inicial de ChatGiPiTi con Gemini API"

# 4. Conectar con tu repositorio remoto y subir
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
```

---

## ✨ Mejoras opcionales (para el futuro)

- 🎙️ **Voz a texto / texto a voz** con `speech_recognition` y `pyttsx3`
- 🌐 **Interfaz web** con Streamlit o Gradio
- 💾 **Persistencia del historial** en un archivo JSON o SQLite
- 🌍 **Soporte multiidioma** con detección automática del idioma del usuario

---

## 📝 Experiencia personal / reflexión

> *(Plantilla para compartir en el Foro #3 de tu curso)*

---

**Nombre:** _Tu nombre aquí_

**¿Qué construiste?**
Una aplicación de consola en Python que usa la Gemini API para chatear de forma conversacional con un asistente amigable.

**¿Qué aprendiste con este proyecto?**
_(Escribe aquí lo que más te sorprendió o te costó: gestión de historial, manejo de errores, variables de entorno, estructura de proyecto…)_

**¿Qué fue lo más difícil?**
_(Por ejemplo: entender cómo funciona la sesión de chat del SDK, o configurar las variables de entorno correctamente.)_

**¿Qué mejorarías?**
_(Por ejemplo: agregar una interfaz web, guardar el historial, soporte de imágenes…)_

**Un consejo para quien empiece este mismo proyecto:**
_(Comparte lo que te hubiera gustado saber antes de empezar.)_

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
