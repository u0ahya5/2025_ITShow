#pip install elevenlabs < 이거 설치하세요
#pip install requests < 얘도 터미널에

from dotenv import load_dotenv
import requests
import os

# 더미 입력값
dummy_request = {
    "voice": "윤성연", #보이스 이름
    "text": "뿅!" #변환할 말
}

# ElevenLabs API 설정

load_dotenv()  # .env 파일 불러오기
eleven_api_key = str(os.getenv("ELEVENLABS_API_KEY"))  # 키 가져오기

def makeVoiceOutput(JSON_FILE):
    VOICE_ID_MAP = {
        "윤성연": "jWRUqvGq5PXd9oOHziob",  # voice ID

        # "윤지쌤": "jWRUqvGq5PXd9oOHziob",  #voice ID
        # "윤환쌤": "jWRUqvGq5PXd9oOHziob",  #voice ID
        # "보경쌤": "jWRUqvGq5PXd9oOHziob",  #voice ID
        # "영철쌤": "jWRUqvGq5PXd9oOHziob",  #voice ID
        # "지웅쌤": "jWRUqvGq5PXd9oOHziob",  #voice ID

        # 다른 목소리도 필요하면 여기에 추가
    }


    voice_name = JSON_FILE["voice"]
    voice_id = VOICE_ID_MAP.get(voice_name)

    if voice_id is None:
        raise ValueError(f"지원하지 않는 voice 이름입니다: {voice_name}")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": eleven_api_key,
        "Content-Type": "application/json"
    }

    data = {
        "text": JSON_FILE["text"],
        "model_id": "eleven_multilingual_v2",  # 또는 필요 시 다른 모델
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    # 요청 및 음성 저장
    response = requests.post(url, json=data, headers=headers, stream=True)

    if response.status_code == 200:
        with open("voice.mp3", "wb") as f:
            for chunk in response.iter_content(chunk_size=4096):
                if chunk:
                    f.write(chunk)
        print("음성 저장 완료: voice.mp3")
    else:
        print(f"오류: {response.status_code}")
        print(response.text)


makeVoiceOutput(dummy_request)

