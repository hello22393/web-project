# 1. Python 기반 이미지
FROM python:3.11-slim

# 2. 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. 작업 디렉토리 설정
WORKDIR /app

# 4. 의존성 설치
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. 프로젝트 복사
COPY . .

# 6. 포트 공개
EXPOSE 8000

# 7. 기본 실행 명령
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
