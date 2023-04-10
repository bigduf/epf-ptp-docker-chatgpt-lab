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

@app.route('/generate_code', methods=['POST'])
def generate_code():
    # Get the JSON data from the request
    data = request.args
    language = data.get('language')
    content = data.get('content')

    # Call OpenAI API to generate code
    completion = openai.ChatCompletion.create(
        engine="davinci-codex",
        prompt=f"Hello Chat, please generate {language} code: {content}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    generated_code = completion['choices'][0]['text']

    # Return generated code as JSON response
    response = {
        'generated_code': generated_code
    }  

    return jsonify(response)
