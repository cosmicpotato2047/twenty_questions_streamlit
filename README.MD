# 🕵️‍♂️ 스무고개 게임

이 리포지토리는 Streamlit과 Ollama LLM을 사용하여 로컬에서 실행하는 스무고개 AI 게임입니다.

## 📦 설치 및 실행

1. 저장소 클론

```bash
git clone https://github.com/cosmicpotato2047/twenty_questions_streamlit.git
cd twenty_questions_streamlit
```

2. 가상환경 생성 및 활성화

```bash
python -m venv venv
# macOS/Linux
type venv/bin/activate && source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. 패키지 설치

```bash
pip install -r requirements.txt
```

4. Ollama 모델 다운로드

```bash
ollama pull llama2:7b
```

5. 앱 실행

```bash
streamlit run main.py
```

브라우저가 자동으로 열리며, “명사 하나를 머릿속에 생각해 주세요.” 버튼을 클릭해 게임을 시작합니다.

## 🎮 게임 규칙

* AI가 영어 명사에 대해 yes/no 질문을 최대 20회 합니다.
* 사용자 답변은 `yes`, `no`, `I don't know`, `it depends`, `quit` 중 하나로 입력합니다.
* AI가 언제든 추측(“Is it a \[object]?”)할 수 있고, 맞추면 AI 승리, 틀리면 AI 패배입니다.
* `quit` 입력 시 즉시 게임이 종료됩니다.
* 게임이 종료된 후 “새 게임 시작” 버튼으로 재도전할 수 있습니다.

## 🗂️ 파일 구조

```
.
├─ main.py            # Streamlit 앱 메인 로직
├─ ollama_llm.py      # Ollama LLM 래퍼 모듈
├─ requirements.txt   # 프로젝트 의존 패키지 목록
└─ README.md          # 프로젝트 소개 및 사용법
```

📝 .gitignore 설정

프로젝트 루트에 .gitignore 파일을 생성하고, Python 관련 캐시 디렉터리와 가상환경 폴더를 제외하도록 아래 내용을 추가하세요:
```
# Python bytecode 캐시
__pycache__/
*.py[cod]

# 가상환경 디렉터리
venv/

# Streamlit 체크포인트
.streamlit/

# 기타
.env
```

## ⚙️ 요구 사항

* Python 3.8 이상
* Ollama CLI ([https://ollama.com](https://ollama.com))
* `requirements.txt`에 명시된 패키지

---

즐거운 게임 되세요! Good luck! 🎉
