"""
AI 자료 요약 자동화기
- articles 폴더의 모든 .txt 파일을 읽어 Gemini API로 자동 요약하고
  하나의 리포트(summary_report.md)로 묶어주는 도구.
"""

import os
from google import genai

# 보안: API 키를 코드에 직접 적지 않고, 환경변수 또는 실행 시 입력으로 받는다
api_key = os.environ.get("GEMINI_API_KEY") or input("Gemini API 키를 입력하세요: ")
client = genai.Client(api_key=api_key)

MODEL = "gemini-3.6-flash"


def summarize(text):
    """기사 한 편을 받아 '핵심요약 3줄 + 한줄결론'으로 요약한다."""
    prompt = f"""다음 글을 한국어로 요약해줘.

형식:
- 핵심요약: 불릿 3개, 각 한 문장
- 한줄결론: 한 문장

글:
{text}"""
    resp = client.models.generate_content(model=MODEL, contents=prompt)
    return resp.text


def main():
    report = "# 자료 요약 리포트\n\n"
    files = sorted(f for f in os.listdir("articles") if f.endswith(".txt"))

    for name in files:
        print(f"요약 중... {name}")
        with open(os.path.join("articles", name), encoding="utf-8") as f:
            content = f.read()
        report += f"## {name}\n\n{summarize(content)}\n\n---\n\n"

    with open("summary_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n완료! 총 {len(files)}개 요약 → summary_report.md 로 저장했습니다.")


if __name__ == "__main__":
    main()
