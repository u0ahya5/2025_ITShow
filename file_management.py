#pip install elevenlabs < 이거 설치하세요
#pip install requests < 얘도 터미널에

from dotenv import load_dotenv
import requests
import os
# ElevenLabs API 설정

load_dotenv()  # .env 파일 불러오기
eleven_api_key = str(os.getenv("ELEVENLABS_API_KEY"))  # 키 가져오기

def makeVoiceOutput(JSON_FILE):

    VOICE_ID_MAP = {
        "윤성연": "jWRUqvGq5PXd9oOHziob",  # voice ID
        "윤지쌤": "TEGif9XnTHchVeIqcots",  #voice ID
        "다연쌤": "DYn4SbPEhzOygOr62bgg",  #voice ID
        "윤환쌤": "VToO2FzplaCc9g1rW2KU",  #voice ID
        "보경쌤": "KK5Kdi6pGnk2nGk099sY",  #voice ID
        "영철쌤": "bbeBsYDC1q79JwuU9hov",  #voice ID
        "지웅쌤": "aw8KVqVoVI3mmUcyPXXz",  #voice ID
        "호식쌤": "HSaoQxZa3a9TnththUL3",  # voice ID
        "태연쌤": "dl7ZwL7RPjznEpmv3tp1"
    }

    voice_name = JSON_FILE["voice"] # 더미 파일에서 voice 이름 가져와 저장
    voice_id = VOICE_ID_MAP.get(voice_name) # 이름에 맞는 voice id 저장

    if voice_id is None:
        raise ValueError(f"지원하지 않는 voice 이름입니다: {voice_name}")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": eleven_api_key,
        "Content-Type": "application/json"
    }

    data = {
        "text": JSON_FILE["text"],
        "model_id": "eleven_multilingual_v2",  # 필요 시 다른 모델로 변경 가능
        "voice_settings": {
            "stability": 1.0,
            "similarity_boost": 1.0,
            "style": 0.75
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



