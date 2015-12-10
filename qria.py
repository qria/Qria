from flask import Flask, render_template, request, g
import json

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


@app.route('/clear_webhook')
def clear_webhook():
    """ initialize webhook list
    """
    g['webhooks'] = []
    return g


@app.route('/view_webhook')
def view_webhook():
    """View all webhooks """
    return g['data']


@app.route('/echo_webhook', methods=['POST'])
def echo_webhook():
    """Echo webhook data and saev it into a list """
    data = json.loads(request.data)
    g['data'].append(data)
    print('webhook:', data)
    return data

if __name__ == '__main__':
    app.run(debug=True)
