
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir google-genai

EXPOSE 8080


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
