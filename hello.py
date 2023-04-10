from flask import Flask,request,jsonify
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/chatgpt')
def chatgpt():
    args = request.args
    message =args.get("message")
    print(message)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion['choices'][0]['message']['content']

@app.route('/generate_code', methods=['GET'])
def generate_code():
    language = request.args.get('language')
    content = request.args.get('content')
    
    if language is None or content is None:
        return "Error: Missing language or content parameter", 400

    prompt=f"Hello Chat, please generate {language} code: {content}"
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion['choices'][0]['message']['content']
