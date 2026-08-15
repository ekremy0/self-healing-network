import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)
TARGET_URL = "http://target_app:5000/health"
CRASH_URL = "http://target_app:5000/crash"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status', methods=['GET'])
def get_status():
    try:
        res = requests.get(TARGET_URL, timeout=0.3)
        if res.status_code == 200:
            return jsonify({"status": "UP"}), 200
        return jsonify({"status": "DOWN"}), 200
    except Exception:
        return jsonify({"status": "HEALING"}), 200

@app.route('/api/attack', methods=['POST'])
def trigger_attack():
    try:
        requests.post(CRASH_URL, timeout=0.5)
        return jsonify({"message": "Attack triggered"}), 200
    except Exception:
        return jsonify({"message": "Target down"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
