# llm

Proyecto sencillo para experimentar con modelos de lenguaje grandes (LLM) ejecutados de forma local usando **Ollama**. Sirve como base para probar prompts, entender cómo consumir una API de LLM desde Python y extenderlo hacia aplicaciones más completas (por ejemplo, asistentes locales o pequeños servicios web).

---

## Descripción del proyecto

Este repositorio contiene un ejemplo mínimo que:

- Se conecta a un servidor local de **Ollama** mediante HTTP.
- Envía una petición con un `prompt` a un modelo de lenguaje (por ejemplo, `gemma3:1b`).
- Recibe la respuesta generada por el modelo y la muestra por consola.

El archivo principal de ejemplo es [aplicaciones/app.py](aplicaciones/app.py), donde se realiza la llamada a la API de Ollama usando la librería `requests`.

Este proyecto está pensado para:

- Practicar el consumo de APIs de modelos de lenguaje desde Python.
- Probar LLMs de forma local sin depender de servicios en la nube.
- Servir como punto de partida para scripts o servicios más avanzados.

---

## Tecnologías utilizadas

- **Python 3**: lenguaje principal del proyecto.
- **requests**: librería HTTP de Python para enviar peticiones `POST` a la API de Ollama.
- **Ollama**: servidor local de modelos de lenguaje, que permite descargar y ejecutar LLMs en la máquina del desarrollador.
- **web.py**, **cheroot** y utilidades relacionadas (listadas en [requirements.txt](requirements.txt)) para futuras extensiones tipo servicio web.

---

## Instalación y configuración

### Requisitos previos

- Python 3 instalado.
- Ollama instalado y corriendo en la máquina.


### 1. Crear y activar un entorno virtual (opcional pero recomendado)

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependencias de Python

```bash
pip install -r requirements.txt
pip install requests
```

> Nota: `requests` puede añadirse también al fichero `requirements.txt` si se quiere dejar registrado.

### 3. Instalar Ollama

En Linux / macOS:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Después de la instalación, asegúrate de que el servicio de Ollama esté en ejecución.

### 4. Descargar el modelo a utilizar

Por ejemplo, para usar `gemma3:1b`:

```bash
ollama pull gemma3:1b
```

---

## Endpoints y ejemplos de uso

Este proyecto consume el endpoint de generación de texto que expone Ollama de forma local.

### Endpoint principal (Ollama)

- **URL base:** `http://localhost:11434`
- **Endpoint de generación:** `/api/generate`
- **Método:** `POST`
- **Content-Type:** `application/json`

### Cuerpo de la petición

Ejemplo de cuerpo mínimo que se envía desde [aplicaciones/app.py](aplicaciones/app.py#L5-L17):

```json
{
  "model": "gemma3:1b",
  "prompt": "hola",
  "stream": false
}
```

### Ejemplo rápido con `curl`

Con Ollama levantado en `http://localhost:11434`, puedes probar el modelo `gemma3:1b` con:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt": "¿Por qué el cielo es azul?",
  "stream": false
}'
```

### Ejemplo en Python (script incluido)

En [aplicaciones/app.py](aplicaciones/app.py) se realiza la misma llamada desde Python:

1. Se define el `prompt` y el modelo a usar.
2. Se envía la petición `POST` a `http://localhost:11434/api/generate` usando `requests`.
3. Se imprime la respuesta generada por el modelo y el nombre del modelo utilizado.

Para ejecutarlo:

```bash
python aplicaciones/app.py
```

---

## Autor

- **Nombre:** Christian Eduardo Navarro Curiel
- **GitHub:** [@christianeduardonavarrocuriel](https://github.com/christianeduardonavarrocuriel)