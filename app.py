from flask import Flask, jsonify, request
from flask_cors import CORS
from get_reply import get_reply

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

@app.route('/word/reply', methods=["POST"])
def cloud():
    text = request.json.get("word")
    res = get_reply(text)
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0')