<div align="center">

```text
  _   _                       _    _               _   
 | \ | | _____  __   _  ___  | |  / \   ___  _ __ | |_ 
 |  \| |/ _ \ \/ /  / |/ _ \ | | / _ \ / _ \| '_ \| __|
 | |\  |  __/>  <   | |  __/ | |/ ___ \ (_) | |_) | |_ 
 |_| \_|\___/_/\_\  |_|\___| |_/_/   \_\___/| .__/ \__|
                                            |_|        
```

**AI-Driven Network Alert Correlation & Noise Reduction POC**

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

</div>

<br/>

<!-- ============================================== -->
<!-- 📷 ADD YOUR DASHBOARD SCREENSHOT RIGHT HERE    -->
<!-- ![Dashboard UI](path/to/image.png)             -->
<!-- ============================================== -->

## Overview
This Proof of Concept (POC) is a lightweight, high-performance Network Operations Center (NOC) dashboard engine. It aggressively reduces "Network Noise" by processing thousands of raw incoming syslogs and leveraging pure Python logic to deduplicate, correlate, and isolate the true underlying root cause.

## Core Features
1. **Deduplication Engine**: Employs a sliding time-window to silence rapidly repeating hardware events.
2. **Alert Correlation**: Ties disparate error strings (e.g., `OSPF Down` & `High Latency`) originating from the same node into a singular, condensed `Incident`.
3. **Root Cause Analysis (RCA)**: Utilizes a custom weighted configuration framework to mathematically prioritize critical hardware failures over secondary symptoms.
4. **Live Traffic Generation**: Includes an isolated `simulator.py` engine generating authentic enterprise log dialects (Cisco IOS / Junos) asynchronously.
5. **Interactive Dashboard**: A glassmorphism dark-mode UI with local JavaScript state trackers mapping the "Acknowledge" and "Resolve" lifecycle without demanding a SQL database.

---

## How to Run Locally

### 1. Pre-requisites & Setup
The central database file for the engine has been explicitly removed from `.gitignore` to prevent pushing massive amounts of raw log data to GitHub. 

**You MUST create the blank destination file before running the script:**
Create an empty file exactly at: `data/alerts.csv`

### 2. Environment Setup
Install the minimal backend requirements (Flask) via your terminal using your preferred python virtual environment:
```bash
pip install -r requirements.txt
```

### 3. Launching the Simulator & API
The system requires executing the generation and processing engines in two completely separate terminals to simulate an asynchronous network environment.

**Terminal 1:** Boot up the processing server API.
```bash
python backend/app.py
```

**Terminal 2:** Boot up the network traffic simulator to begin dumping logs into your newly created `.csv` file.
```bash
python simulator.py
```

### 4. Open the Interface
Using your native desktop directory, double-click `frontend/index.html` to open it in any modern browser. The frontend Dashboard relies entirely on native browser API's pulling from `localhost:5000` via Javascript every 5 seconds, so no NPM dependencies or Node.js required!
