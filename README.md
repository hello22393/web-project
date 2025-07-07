# web-project
# 프로젝트 평가 웹사이트

이 프로젝트는 Django와 Docker를 이용하여 구현된 웹 기반 프로젝트 평가 시스템입니다.  
관리자는 프로젝트를 등록하고, 사용자는 프로젝트를 평가할 수 있으며, 평가 결과를 평균 점수 순으로 실시간으로 확인할 수 있습니다.

---

## 주요 기능

### 관리자 기능
- 프로젝트 제목과 상세 설명 입력
- 관리자 페이지에서 모든 프로젝트 및 평가 결과 확인
- 평균 점수 기준으로 프로젝트 정렬 가능

### 사용자 기능
- 홈페이지에서 전체 프로젝트 리스트 확인
- 프로젝트 상세 페이지에서 1~5점 평가 가능
- 투표 후 평균 점수 및 투표 수 결과 확인

---

##  사용 기술

- **Python 3.10**
- **Django**
- **SQLite**
- **Docker / Docker Compose**
- **HTML (템플릿)**

---

## 프로젝트 구조
web-project/
├── config/               # Django 설정
├── projects/             # 프로젝트 평가 앱
│   └── templates/        # HTML 템플릿
├── db.sqlite3            # 기본 DB
├── manage.py             # Django 명령어 진입점
├── Dockerfile            # Docker 이미지 설정
├── docker-compose.yml    # Docker 실행 설정
├── requirements.txt      # Python 패키지 목록

---

## 실행 방법

# 개발용으로 실행하는 방법 (Windows 기준)
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1

# 패키지 설치
pip install -r requirements.txt

# 서버 실행
python manage.py runserver

#관리자 계정 생성
python manage.py createsuperuser
```

## Docker로 실행하는 방법
```bash
# 1. 이미지 빌드 및 컨테이너 실행
docker-compose up --build

# 2. 웹사이트 접속
http://localhost:8000

# 3. 관리자 페이지 접속
http://localhost:8000/admin
```
