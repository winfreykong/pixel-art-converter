from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

# @app.route("/generate", methods=['POST'])
# def generate_response():
#     print(request.form)
#     custom_webpath = request.form['custom_webpath']
#     question = str(request.form['question'])

#     print("### Initializing environment and creating model...")
#     model = initialize_env_and_model()
#     print("### Parsing webpath...")
#     model([custom_webpath], use_strainer=True, strainer_class='s-lib-box-content')
#     print(f"### Generating response to question: {question}")
#     answer = model.ask(question)

#     return render_template('index.html', output=answer)

if __name__ == "__main__":
    app.run()