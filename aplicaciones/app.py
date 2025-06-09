import requests
import json

data = {
  "model": "gemma3:1b",
  "prompt":"hola",
  "stream": False
}

url= "http://localhost:11434/api/generate"

response = requests.post(url,json=data)

response = json.loads(response.text)

print(response["response"])
print(response["model"])