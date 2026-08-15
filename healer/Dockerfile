FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir requests docker
COPY healer.py .
CMD ["python", "healer.py"]
