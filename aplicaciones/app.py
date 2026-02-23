import requests
import json

# Cuerpo de la petición que se enviará a la API de Ollama.
# - "model": nombre del modelo que queremos usar.
# - "prompt": texto que el modelo va a procesar.
# - "stream": si es False, la respuesta llega de una sola vez.
data = {
  "model": "gemma3:1b",
  "prompt": "hola",
  "stream": False
}

# URL del endpoint de generación de texto de Ollama
url = "http://localhost:11434/api/generate"

# Enviamos una petición POST a la API, pasando el JSON con los datos.
response = requests.post(url, json=data)

# Convertimos el texto de la respuesta HTTP a un diccionario de Python.
response = json.loads(response.text)

# Mostramos por pantalla el texto generado por el modelo.
print(response["response"])

# Mostramos el nombre del modelo que se usó para generar la respuesta.
print(response["model"])