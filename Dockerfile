FROM python:3.11-slim

WORKDIR /app

COPY api.py .

CMD ["python", "api.py"]
