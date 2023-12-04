from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KubaJeFrajer'
socketio = SocketIO(app)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    socketio.emit('message', message)


if __name__ == '__main__':
    socketio.run(app, debug=True)
