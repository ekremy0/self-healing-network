# 🛡️ Self-Healing Autonomous Resilience Network
# 🛡️ Autonomous Self-Healing Infrastructure
> **A zero-trust, microservice-level resilient network capable of detecting catastrophic failures and executing sub-second autonomous hot-restarts via direct Docker Socket interactions.**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Resilience](https://img.shields.io/badge/Self--Healing-Sub--Second-brightgreen?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-Microservices-orange?style=for-the-badge)

---

## 💡 Executive Summary & Core Value Proposition

In modern cloud-native environments (FinTech, E-Commerce, High-Frequency Trading), **downtime directly equals financial loss**. Standard incident response frameworks rely on telemetry pipelines (Prometheus/Grafana) and human ops intervention, typically yielding a **5 to 15-minute Mean Time to Recovery (MTTR)**.

This project introduces a **Self-Healing Resilience Agent** operating at the edge of the container ecosystem. By continuously auditing container vitality via high-frequency health pings, the agent dynamically traps HTTP `500` errors or container panics, executing an **autonomous hot-restart in < 1000ms**.

---

## ⚙️ System Architecture & Data Flow

The infrastructure is orchestrator-agnostic, built using a fully containerized three-tier microservice architecture:

                      +-----------------------------------+
                      |      Interactive Dashboard        |
                      |       (Port 8080 - HTML5)         |
                      +-----------------+-----------------+
                                        |
                                        v
+-----------------------+     Heartbeat Audit (300ms)     +-----------------------+
|   Target Microservice | <---------------------------------- |   Autonomous Healer   |
|   (Flask Web App)     |                                     |   (Watcher Agent)     |
+-----------+-----------+                                     +-----------+-----------+
|                                                             |
| (Triggers Panic / Crash)                                    | Issues Repair Command
v                                                             v
[ STATE: DOWN ] <======================================== [ Unix Docker Socket ]


### 🧩 Microservice Breakdown

1. **`target_app` (Victim Node):** A lightweight Python/Flask core microservice handling application traffic (`/health` and `/crash` simulated attack vectors).
2. **`healer_agent` (Autonomous Repairer):** A background watcher bot that pings the target node every 300ms. If the target fails to respond, the agent directly interacts with the host's `/var/run/docker.sock` to force-restart the broken container.
3. **`dashboard_panel` (Command Center):** An asynchronous UI providing real-time system monitoring, status transition visualization, and a manual threat injection button.

---

## ⚡ Real-World SLA Comparison

| Metric | Traditional Incident Response | Self-Healing Resilience Network |
| :--- | :--- | :--- |
| **Detection Time** | 1 - 5 Minutes (Alerting Thresholds) | **< 300 Milliseconds** |
| **Human Intervention** | Required (On-Call Engineer) | **Zero (100% Autonomous)** |
| **Recovery Time (MTTR)** | 5 - 30 Minutes | **< 1 Second** |
| **Business Impact** | High Revenue Loss & SLA Violation | **Negligible Impact / High Availability** |

---

## 🚀 Quick Deployment Guide

Deploy the entire self-healing ecosystem on any host machine in three simple steps:

### Prerequisites
* **Docker Engine** (>= 20.10)
* **Docker Compose** (>= 2.0)

### Execution

```bash
# 1. Clone the repository
git clone [https://github.com/ekremy0/self-healing-network.git](https://github.com/ekremy0/self-healing-network.git)

# 2. Enter project directory
cd self-healing-network

# 3. Launch the containerized cluster
docker compose up --build -d
Access the visual Command Center at: http://localhost:8080

🧪 Threat Simulation Protocol
Open http://localhost:8080 in your web browser. Observe the active system status: ✅ SİSTEM SAĞLIKLI (200 OK).

Click ⚡ SİBER SALDIRI BAŞLAT to simulate a critical process failure on the target application.

Observe the immediate state sequence:

🚨 CRITICAL: Application node crashes.

🔄 HEALING: The Healer Agent detects failure and triggers container recovery via Docker Socket.

✅ HEALTHY: Application restored to full operational state in < 1s.

🛠️ Tech Stack & Concepts
Infrastructure & Containerization: Docker, Docker Compose, Unix Socket Interoperability (/var/run/docker.sock)

Core Logic & Services: Python 3.11, Flask, Requests Engine, Docker SDK

Frontend Telemetry: Dynamic HTML5, Responsive Glassmorphism CSS, Async Fetch API
