import cohere
from dotenv import load_dotenv
import random
import os

load_dotenv()  # .env 파일 불러오기
api_key = os.getenv("COHERE_API_KEY")  # 키 가져오기

co = cohere.Client(api_key)


# 더미 프론트에서 받아올 JSON 형식
dummy_request = {
    "name" : "한지연",
    "worry" : "대충 입력한 고민",
    "department" : "S" # 학과 S,D (답변 해주실 선생님을 분류하기 위함)
}

def makePrompt(JSON_FILE):
    userName = JSON_FILE["name"]
    userWorry = JSON_FILE["worry"]
    userDepartment = JSON_FILE["department"]

    teachersPrompt = {
        "윤지쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성",
        " ": "",
        "윤환쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성",
        "보경쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성",
        "영철쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성",
        "지웅쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성"
        # 다른 목소리도 필요하면 여기에 추가
    }

    #menu = int(input("1. 그리핀도르 2. 슬리데린 3. 레번클로 4. 후플푸프 : "))

    if(userDepartment == "S"): #솦과 (디자인과쌤 제외)
        randomNumber = random.randint(1, 5)
    else: #디자인과 (솦과쌤 제외)
        randomNumber = random.randint(5, len(teachersPrompt))




response = ""

# 말투 프롬프트 (예 : 해리포터 기숙사)
if menu == 1 : #그리핀도르
    response = co.chat(message="역할 : 용기 있고 열정적인 상담자 역할이에요. 직접적으로 말하지만 무례하진 않아요. 상대가 힘낼 수 있도록 응원하는 톤으로 말해요. 한 문장으로 대답해줘. 질문 : "+ question)
elif menu == 2 : #슬리데린
    response = co.chat(message="역할 : 전략적이고 현실적인 상담자야. 차가워 보일 수 있지만, 실질적인 해결책에 집중하며 솔직하고 단호하게 말해요. 약간의 냉소나 여유도 허용됨. 한 문장으로 대답해줘. 질문 : "+question)
elif menu == 3 : #레번클로
    response = co.chat(message="역할 : 이성적이고 논리적인 상담자 역할이에요. 침착하고 신중한 말투로 조언을 줍니다. 말은 예의 바르되 약간 객관적인 시선을 유지합니다. 한 문장으로 대답해줘. 질문 : "+question)
elif menu == 4 : #후플푸프
    response = co.chat(message="역할 : 너는 따뜻하고 친절한 상담자야. 항상 상대를 배려하고, 다정하게 공감해줘. 존댓말을 쓰되 너무 딱딱하진 않고, 부드럽고 위로가 되는 말투로 말해. 한 문장으로 대답해줘. 질문 : "+question)
else :
    response = co.chat(message=question)

print("상담봇 :", response.text)
