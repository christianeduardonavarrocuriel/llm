# llm
Repositorio para hacer mi propia I.A con "Modelos de Lenguaje Largo"

## Comando para instalar **Ollama**:
```shell
curl -fsSL https://ollama.com/install.sh | sh
```
## Comando para generar:

```shell
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt":"Por que el cielo es azul?"
}'
```