import sys
from flask import Flask, jsonify, request

app = Flask(__name__)
IS_HEALTHY = True

@app.route('/')
def home():
    if not IS_HEALTHY:
        return jsonify({"status": "CRITICAL_FAILURE", "message": "System compromised or crashed!"}), 500
    return jsonify({"status": "OPERATIONAL", "message": "Service is running normally."}), 200

@app.route('/health', methods=['GET'])
def health():
    if IS_HEALTHY:
        return jsonify({"status": "UP"}), 200
    return jsonify({"status": "DOWN"}), 500

@app.route('/crash', methods=['POST'])
def crash():
    global IS_HEALTHY
    IS_HEALTHY = False
    return jsonify({"status": "FATAL", "message": "Simulated attack payload executed. System crashed!"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
