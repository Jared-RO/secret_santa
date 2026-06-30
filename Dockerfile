# 1. Imagen base ligera
FROM python:3.11-slim

# 2. Variables de entorno de Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Directorio de trabajo
WORKDIR /app

# 4. Instalamos Git (indispensable para clonar secret_santa_logic durante el build)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# 5. Copiamos el archivo de configuración del proyecto
COPY pyproject.toml .
# Si tienes un README.md vacío o con texto, cópialo también porque lo pide el toml
COPY README.md* .

# 6. Actualizamos pip e instalamos las dependencias definidas en el pyproject.toml
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

# 7. Copiamos el resto del código fuente del backend
COPY backend/ .

# 8. Exponer puerto (informativo)
EXPOSE 8000

# 9. Comando de arranque
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
