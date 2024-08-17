import openai
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# .env에서 API 키 가져오기
openai.api_key = os.getenv("OPENAI_API_KEY")

# 이후 OpenAI API를 호출하는 코드
def correct_text(user_input):
    prompt = f"Please correct the spelling and grammar of the following text: '{user_input}'"
    
    # GPT-3 모델에 교정 요청
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT 모델 선택
        prompt=prompt,
        max_tokens=500
    )
    
    # ChatGPT가 수정한 텍스트 추출
    corrected_text = response.choices[0].text.strip()
    return corrected_text

# 사용자 입력
user_input = input("교정할 텍스트를 입력하세요: ")

# 맞춤법 및 문맥 교정
corrected_text = correct_text(user_input)

# 결과 출력
print(f"수정된 텍스트: \n{corrected_text}")
