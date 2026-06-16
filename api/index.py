import os
from dotenv import load_dotenv
from google import genai
from flask import Flask, request, jsonify
from flask_cors import CORS

# .env file se variables ko load karna
load_dotenv()

app = Flask(__name__)
CORS(app)

# Khupiya file se API key uthana
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Client initialize karna
client = genai.Client(api_key=GEMINI_API_KEY)

@app.route('/api/summarize', methods=['POST'])
def summarize():
    data = request.json
    user_text = data.get('text', '')
    
    try:
        prompt = f"Summarize the following study notes in simple, easy-to-understand terms with bullet points:\n\n{user_text}"
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return jsonify({'result': response.text})
    except Exception as e:
        return jsonify({'result': f"Error calling Gemini AI: {str(e)}"})

@app.route('/api/flashcards', methods=['POST'])
def flashcards():
    data = request.json
    user_text = data.get('text', '')
    
    try:
        prompt = f"Create a list of Question and Answer flashcards based on this text. Keep it concise and practical:\n\n{user_text}"
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return jsonify({'result': response.text})
    except Exception as e:
        return jsonify({'result': f"Error calling Gemini AI: {str(e)}"})

if __name__ == '__main__':
    # Cloud server dynamic port deta hai, isliye os se port read karenge
    import os
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' likhna zaroori hai taaki server bahar se accessible ho
    app.run(host='0.0.0.0', port=port)