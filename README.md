# AI 자료 요약 자동화기 

여러 개의 텍스트 자료(기사·보고서 등)를 한 번에 읽어, Gemini API로 자동 요약하고 하나의 리포트로 묶어주는 파이썬 도구입니다.

##  만든 이유
자료를 하나하나 열어 읽고 요약하는 일은 반복적이고 시간이 많이 듭니다.
폴더에 파일을 넣기만 하면 알아서 요약 리포트가 나오도록 만들면,
사람은 읽고 판단하는 핵심 작업에만 집중할 수 있습니다.
이 반복 업무를 자동화하기 위해 만든 도구입니다.

##  주요 기능
- `articles/` 폴더의 모든 `.txt` 파일을 자동으로 읽음
- 각 자료를 Gemini API로 "핵심요약 3줄 + 한줄결론" 형식으로 요약
- 전체 결과를 하나의 `summary_report.md` 리포트로 자동 저장

##  작동 방식
1. 폴더에서 텍스트 파일 목록을 불러온다
2. 각 파일 내용을 Gemini API(`gemini-3.6-flash`)에 보내 요약을 받는다
3. 요약들을 마크다운 리포트로 합쳐 파일로 저장한다

## ▶️ 사용 방법
1. 라이브러리 설치: `pip install google-genai`
2. Google AI Studio에서 Gemini API 키 발급 (무료)
3. `articles/` 폴더에 요약할 `.txt` 파일 넣기
4. 실행: `python ai_summarizer.py` (실행 시 API 키 입력)
5. 생성된 `summary_report.md` 확인

##  사용 기술
- Python
- Google Gemini API (`google-genai`)

---
반복적인 자료 요약 업무를 AI를 코드에 연결해 자동화한 프로젝트입니다.
