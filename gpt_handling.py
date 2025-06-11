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
    userName = JSON_FILE["name"] # 사용자 이름
    userWorry = JSON_FILE["worry"] # 사용자 고민
    userDepartment = JSON_FILE["department"] # 학과

    teachersPrompt = { # 선생님과 말투 프롬프트 (~하는 말투로 끝내기)
        "윤지쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성",
        "다연쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성",
        "윤환쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성",
        "보경쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성",
        "영철쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성",
        "지웅쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성",
        "호식쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성"
        # 다른 목소리도 필요하면 여기에 추가
    }
    
    prompts = list(teachersPrompt.items())  # 튜플 리스트 [(이름, 프롬프트), ...]

    # 학과에 따른 분류
    if userDepartment == "S":
        selected_teachers = prompts[0:6]  # 솦과
    elif userDepartment == "D":
        selected_teachers = prompts[2:]  # 디자인과
    else:
        selected_teachers = prompts  # 전체 중에서

    selected_teacher = random.choice(selected_teachers)
    voice_name = selected_teacher[0]  # voice 이름
    prompt = selected_teacher[1] # voice 프롬프트

    # AI에게 전달할 메시지 생성
    chat_message = f"{userWorry}, 이것이 {userName}의 고민이야. {prompt} 한 줄 정도의 짧은 고민 해결 답안을 제시해줘."

    response = co.chat(message=chat_message)
    text = response.text.strip() # ai 답변

    return {
        "voice": voice_name,
        "text": text
    }

result = makePrompt(dummy_request)
print(result)
