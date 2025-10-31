# 1. 베이스 이미지
FROM python:3.11-slim

# 2. 작업 디렉토리
WORKDIR /app

# 3. 필요 파일 복사
COPY . .

# 4. 의존성 설치
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir google-genai

# 5. 포트 노출
EXPOSE 8080

# 6. FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
