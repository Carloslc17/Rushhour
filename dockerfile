# Importar python
FROM python:3.12-slim
# Evitar .pyc y buffering
ENV PYTHONDONTWRITEBYTECODE=1 \PYTHONUNBUFFERED=1
# Directorio principal
WORKDIR /app
# Copiar dependencias
COPY requirements.txt .
# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt
# Copiar todo el codigo
COPY . .
# Comando por defecto
ENTRYPOINT ["python", "-m", "rushhour.main"]

