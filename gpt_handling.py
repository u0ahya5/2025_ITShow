from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import cohere
import os
import random
import base64

from file_management import makeVoiceOutput

app = Flask(__name__)
CORS(app)

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key)

def makePrompt(JSON_FILE):
    userName = JSON_FILE["name"]
    userWorry = JSON_FILE["worry"]
    userDepartment = JSON_FILE["department"]

    teachersPrompt = {
        "윤지쌤": "감정적인 공감을 해주시는 차분하고 귀여운 말투로",
        "다연쌤": "장난스럽게 감정보단 이성적인 판단으로 현실적인 조언을 해주는 말투로",
        "윤환쌤": "장난스러운데 약간 진지한 면이 있고 오글거리지 않게 자유로운 조언을 해주는 말투로 ",
        "보경쌤": "차분하고 엄마같이 마음을 헤아려주지만 현실적인 조언도 같이 제시 해주는 말투로",
        "영철쌤": "무뚝뚝한데 약간 유쾌한 말투로 이름을 넣어서 고민의 이유를 추론하고 현실적인 조언을 툭 던지듯한 말투로",
        "지웅쌤": "여기에 성격과 말투를 나타내는 프롬프트 작성",
        "호식쌤": "직설적인 말투로 팩트를 얘기하며 정신이 번쩍 들 수 있는 따끔한 멘트로",
        "태연쌤": "친근하고 따뜻한말투지만 쿨하게 적당한 공감과 적당한 해결책을 제시해주는 말투로"
    }

    prompts = list(teachersPrompt.items())

    if userDepartment == "S":
        selected_teachers = prompts[0:6]
    elif userDepartment == "D":
        selected_teachers = prompts[1:]
    else:
        selected_teachers = prompts

    selected_teacher = random.choice(selected_teachers)
    voice_name = selected_teacher[0]
    prompt = selected_teacher[1]

    chat_message = f"{userWorry}, 이것이 {userName}의 고민이야. {prompt} 한 줄 정도의 짧은 고민 해결 답안을 제시해줘."

    response = co.chat(message=chat_message)
    text = response.text.strip()

    return {
        "voice": voice_name,
        "text": text
    }

@app.route('/make-prompt', methods=['POST'])
def handle_prompt():
    try:
        json_data = request.get_json()
        result = makePrompt(json_data)

        # 음성 생성
        makeVoiceOutput(result)  # voice.mp3 생성됨

        # voice.mp3 파일을 base64로 변환
        with open("voice.mp3", "rb") as f:
            audio_base64 = base64.b64encode(f.read()).decode('utf-8')

        # JSON 응답으로 음성과 정보 함께 전송
        return jsonify({
            "voice": result["voice"],
            "text": result["text"],
            "audio": audio_base64
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
