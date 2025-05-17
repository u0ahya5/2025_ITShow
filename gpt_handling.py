import cohere
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일 불러오기
api_key = os.getenv("COHERE_API_KEY")  # 키 가져오기

co = cohere.Client(api_key)

question = input("고민을 입력하세요 : ")
response = co.chat(message = question)
print("상담봇 :", response.text)
