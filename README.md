# Laboratorio de orquestadores de contenedores

Imagen en dockerHub disponible con `docker pull isaacamador/traductor_genai:latest`

Evidencia en la carpeta de `capturas/

## Instrucciones para ejecutar

### Ejecutar con Docker Compose

1. Ingresar a la carpeta de infraestructura
```bash
cd infra/
```
2. Crea la variable de entorno para la API key de Gemini
```bash
# Exporta la variable en la terminal
export GEMINI_API_KEY=su_api_key
```
3. Construir y montar la imagen con docker compose
```bash
docker compose up --build
```

### Ejecutar con Docker Swarm

1. Ingresar a la carpeta de infraestructura
```bash
cd infra/
```
2. Crea la variable de entorno para la API key de Gemini
```bash
# Exporta la variable en la terminal
export GEMINI_API_KEY=su_api_key
```
3. Ejecutar el stack
```bash
docker stack deploy -c docker-stack.yml traductor_genai
```
Ver el estado de los servicios
```bash
docker stack services traductor_genai 
```

### Ejecutar de manera Local
1. Ingresar a la carpeta de la app
```bash
cd gradio_app/
```
2. Crear un entorno virtual de Python 
```bash
python3 -m venv venv
```
3. Activar entorno virtual windows: 
    En windows:
    ```bash
    venv\Scripts\activate
    ```
    En linux :
    ```bash
    source venv/bin/activate
    ```
4. Instalar dependencias 
```bash
pip install -r requirements.txt
```
5. Ejecutar el script principal 
```bash
python app.py
```




