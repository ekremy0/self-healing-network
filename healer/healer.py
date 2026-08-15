import time
import requests
import docker

client = docker.from_env()
TARGET_URL = "http://target_app:5000/health"
CONTAINER_NAME = "target_app"

def check_and_heal():
    print("[HEALER ACTIVE] Monitoring target application status...", flush=True)
    while True:
        try:
            response = requests.get(TARGET_URL, timeout=0.5)
            if response.status_code != 200:
                print(f"\n[ALERT] System Failure Detected! Status: {response.status_code}", flush=True)
                heal_system()
        except Exception as e:
            print("\n[ALERT] Connection Lost! Target App Unreachable.", flush=True)
            heal_system()
        
        time.sleep(0.3)

def heal_system():
    start_time = time.time()
    print("[HEALING STARTED] Executing autonomous recovery...", flush=True)
    try:
        container = client.containers.get(CONTAINER_NAME)
        container.restart()
        recovery_time = (time.time() - start_time) * 1000
        print(f"[HEALING COMPLETED] System successfully recovered in {recovery_time:.2f} ms!\n", flush=True)
    except Exception as err:
        print(f"[ERROR] Healing sequence failed: {err}", flush=True)

if __name__ == "__main__":
    time.sleep(3)
    check_and_heal()
