# 공공임대주택 정보 안내 도우미 – 찾아줘 홈즈 🏠
<img src="./images/홈즈.png" width="800" height="450">

## 📌 프로젝트 개요
본 프로젝트는 어르신의 과거 사진을 기반으로 회상 대화를 유도하고, 해당 음성 및 텍스트 데이터를 분석하여 치매의 조기 징후를 비침습적으로 탐지하는 AI 기반 정서 돌봄 서비스입니다.<br/>
회상 대화를 통해 인지·정서 상태를 자연스럽게 평가하고, 보호자에게 이상 징후를 리포트 및 스토리 형태로 제공하는 것을 목표로 합니다.<br/>
**본 시스템은 다음과 같은 기술적 구성요소로 이루어져 있습니다**
- LLM 기반 GPT-4o: 대화 내용 요약 및 감정 분석, 정서 이상 탐지
- Xception 기반 CNN 모델: 음성에서 치매 위험도 분류
- FastAPI + PostgreSQL + Docker 기반 백엔드
- Azure Virtual Machine 상에서 상시 운영

## 👀 How does it work?

<div align="center">
  <img src="./images/demo1.gif" width="45%" style="margin-right: 10px;" />
  <img src="./images/demo2.gif" width="45%" />
</div>

## ⚙️ Architecture

<img src="./images/architecture.png" style="width: 100%; height: auto;" />


## 🛠️ 기술 스택
<img src="https://img.shields.io/badge/Azure OpenAI-0078D4?style=flat-square&logo=OpenAI&logoColor=white"/> <img src="https://img.shields.io/badge/Azure Document Intelligence-0078D4?style=flat-square&logo=&logoColor=white"/> <img src="https://img.shields.io/badge/Azure AI Search-0078D4?style=flat-square&logo=&logoColor=white"/> <img src="https://img.shields.io/badge/Azure Virtual Machine-0078D4?style=flat-square&logo=&logoColor=white"/> <br/><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/flask-000000?style=flat-square&logo=flask&logoColor=white"/> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/> <img src="https://img.shields.io/badge/ngrok-1F1E37?style=flat-square&logo=ngrok&logoColor=white"/> <img src="https://img.shields.io/badge/Kakaotalk-FFCD00?style=flat-square&logo=kakaotalk&logoColor=white"/> 


- **Azure OpenAI** : embedding 모델을 통한 벡터화 및 GPT-4 기반 언어 모델을 사용해 자연어 응답 생성
- **Azure Document Intelligence Layout** : PDF을 Markdown 파일로 변환
- **Azure AI Search** : 벡터 기반 유사도 검색으로 관련 공고문 청크를 반환
- **Azure VM** : Python 기반 Flask 서버를 가상머신에서 상시 운영
- **Flask** : 로컬 서버 생성
- **Ngrok** : 로컬/VM 서버를 카카오톡 챗봇에서 접근 가능하도록 터널링
- **LangChain**: 텍스트 분할, 임베딩 및 RAG 파이프라인 구성
- **Python**: 전체 백엔드 및 데이터 전처리 로직 작성
- **Kakao i 오픈빌더**: 사용자 인터페이스 챗봇 구성
<br/>

## 🗂️ 프로젝트 구조
### Backend
#### Fastapi
**`fastapi-app\app\`**
- `main.py`: FastAPI 서버 메인 엔트리포인트
- `db\models\`: DB 테이블 정의 (SQLAlchemy)
- `schemas\` : API용 데이터 모델 정의 (Pydantic)
- `routers\` : API 엔드포인트 정의
- `services\` : 비즈니스 로직 처리
#### Fish-Speech 
**`fastapi-app\fish-speech\`**
- `fish_main.py` : main 모듈
- `fish_module.py` : 추론 모듈
- `preprocessing.py` : 전처리 모듈

### Frontend
**`Front\lib\`**
- `screens\` : UI 화면 구성 
- `models\` : 도메인 객체 정의


## 🎯 주요 기능
> **가족 전용 커뮤니티** : family_id를 활용해 가족 간 회상 콘텐츠를 비공개로 공유하고 열람할 수 있는 공간 제공
> **회상 대화 기반 치매 조기 탐지** : 사진 기반 회상 대화를 통해 자연스러운 대화를 유도
- voice -> text -> gpt -> text -> voice로 이루어지는 파이프라인을 통한 자연스러운 음성 대화 로직 구현
> **보호자 알림 리포트 제공** : 대화 요약, 감정 상태, 발화 특성 등 분석 리포트 생성<br/>
> **스토리텔링 생성** : 대화 데이터를 활용하여 사진에 대한 스토리텔링 생성<br/>
> **voice cloning** : 환자의 음성데이터를 cloning하여 환자의 목소리로 스토리 읽어줌<br/>

### 🎥 시연영상 
- [📷 시연영상 보기!](https://github.com/hongwon1031/MS_AI_project_2/blob/main/%EC%B9%B4%ED%86%A1%EC%8B%9C%EC%97%B0%EC%98%81%EC%83%81.mp4)<br/>
- [📷 홍보영상 보기!](https://github.com/hongwon1031/MS_AI_project_2/blob/main/%EC%8B%9C%EC%97%B0%EC%98%81%EC%83%81.mp4)
### 자세한 내용은 [[복덕방7]발표.PDF](https://github.com/hongwon1031/MS_AI_project_2/blob/main/%5B%EB%B3%B5%EB%8D%95%EB%B0%A97%5D%EB%B0%9C%ED%91%9C.pdf) 참고
### 🐶 How to use?
~~[카카오톡 채널](http://pf.kakao.com/_QfZwn) 혹은 카카오톡에서 '찾아줘! 홈즈' 검색~~
- azure 리소스 삭제로 인해 현재 사용 불가능

backend
docker-compose up build
