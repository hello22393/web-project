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

## 실행 방법

## 로컬에서 실행하는 방법 (Windows 기준)

```bash
# 1. 가상환경 생성
python -m venv venv

# 2. 가상환경 활성화
.\venv\Scripts\activate

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 마이그레이션 적용
python manage.py migrate

# 5. 관리자 계정 생성
python manage.py createsuperuser

# 6. 개발 서버 실행
python manage.py runserver

# 2. 웹사이트 접속
http://localhost:8000

# 3. 관리자 페이지 접속
http://localhost:8000/admin
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
