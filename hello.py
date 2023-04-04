from flask import Flask, request
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
    message = args.get("message")
    print(message)
    completion = openai.ChatCompletion.create(
        model="text-davinci-002",
        prompt=message,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None
    )
    return completion['choices'][0]['text']

@app.route('/generate_code')
def generate_code():
    args = request.args
    coding_language = args.get("coding_language")
    code_request = args.get("code_request")

    message = f"Write {code_request} in {coding_language}."
    print(message)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion['choices'][0]['message']['content']
