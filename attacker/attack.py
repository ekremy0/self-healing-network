import time
import requests

TARGET_URL = "http://target_app:5000/crash"

print("[ATTACKER READY] Attack simulation module loaded.", flush=True)
print("[ATTACKER] Waiting 10 seconds before initiating cyber attack...", flush=True)
time.sleep(10)

print("\n[ATTACK LAUNCHED] Sending malicious payload to target application...", flush=True)
try:
    response = requests.post(TARGET_URL, timeout=2)
    print(f"[ATTACK SUCCESSFUL] Server Response: {response.status_code} - {response.text}", flush=True)
except Exception as e:
    print(f"[ATTACK FAILED/EXECUTED] Trigger sent: {e}", flush=True)
