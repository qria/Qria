from flask import Flask, render_template, request, g
import json

from vocabulary import analyze_hard_vocabulary

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/api/message')
def send_message():
    message = request.args.get('message', None)
    if not message:
        return 'message is required!'
    return 'message sent! %s' % message


@app.route('/echo_webhook', methods=['POST'])
def echo_webhook():
    """Echo webhook data """
    data = json.loads(request.data.decode())
    print('Webhook received:', data)
    return str(data)


@app.route('/text_analyzer', methods=['GET', 'POST'])
def text_analyzer(text=None):
    text = 'Hello horrifying world!'
    if text:
        definitions = analyze_hard_vocabulary(text)
        return str(definitions)
    return 'hi'


if __name__ == '__main__':
    app.run(debug=True)
