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


@app.route('/generate-code')
def generate_code():
    args = request.args
    language = args.get("language")
    content = args.get("content")
    prompt = f"Generate code in {language} programming language based on the following content:\n\n{content}\n\nCode:"
    completion = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return completion.choices[0].text.strip()


if __name__ == "__main__":
    app.run(debug=True)

