from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homePage():
    return jsonify({"status":"this is the front end"})

@app.route('/status', methods=['GET'])
def check_status():
    return jsonify({"status": "Server is ready"}), 200

if __name__ == '__main__':
    app.run()
