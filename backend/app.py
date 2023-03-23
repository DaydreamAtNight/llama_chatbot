from flask import send_from_directory
from flask import Flask, jsonify, request
from flask_cors import CORS
from get_reply import get_reply
import os

# # configuration
# DEBUG = True

# instantiate the app
app = Flask(__name__, static_folder="../frontend/dist/")
app.config.from_object(__name__)

# enable CORS
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/word/reply', methods=["POST"])
def cloud():
    text = request.json.get("word")
    res = get_reply(text)
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0')