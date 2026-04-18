<div align="center">
<pre>
███████╗██╗  ██╗██╗  ██╗██╗     ███████╗██████╗ ████████╗
██╔════╝██║  ██║██║  ██║██║     ██╔════╝██╔══██╗╚══██╔══╝
███████╗███████║███████║██║     █████╗  ██████╔╝   ██║   
╚════██║██╔══██║██╔══██║██║     ██╔══╝  ██╔══██╗   ██║   
███████║██║  ██║██║  ██║███████╗███████╗██║  ██║   ██║   
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   

  by NeRDs — **Ne**twork **R**isk **D**efender**s**
</pre>
</div>

<div align="center">
  
**Alert Correlation & Noise Reduction for Network Operations**

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



Shhlert is a Proof of Concept (POC) Network Operations Center (NOC) dashboard engine. It aggressively reduces **network noise** by ingesting thousands of raw syslogs and applying pure Python logic to deduplicate, correlate, and surface the true underlying root cause of every incident.

---

## Core Features

| Feature | Description |
|---|---|
| 🔕 **Deduplication Engine** | Sliding time-window silences rapidly repeating hardware events |
| 🔗 **Alert Correlation** | Ties disparate errors (e.g. `OSPF Down` + `High Latency`) from the same node into a single condensed `Incident` |
| 🎯 **Root Cause Analysis** | Weighted configuration framework mathematically prioritizes critical hardware failures over secondary symptoms |
| 📡 **Live Traffic Generation** | `simulator.py` asynchronously generates authentic Cisco IOS / Junos enterprise log dialects |
| 🖥️ **Interactive Dashboard** | Glassmorphism dark-mode UI with JS state trackers handling the full `Acknowledge → Resolve` alert lifecycle — no SQL required |

---

## Getting Started

### Prerequisites

> **Important:** The `data/alerts.csv` file is excluded from `.gitignore` to prevent large log dumps from being committed. You must create it manually before running anything.

```bash
mkdir -p data && touch data/alerts.csv
```

### 1. Install Dependencies

Set up a Python virtual environment, then install the minimal backend requirements:

```bash
pip install -r requirements.txt
```

### 2. Start the Backend API

In **Terminal 1**, launch the processing server:

```bash
python backend/app.py
```

### 3. Start the Traffic Simulator

In **Terminal 2**, start generating synthetic network logs:

```bash
python simulator.py
```

> The simulator and API run in separate terminals to replicate a true asynchronous network environment.

### 4. Open the Dashboard

Open `frontend/index.html` directly in any modern browser — no Node.js or npm required. The frontend polls `localhost:5000` every **5 seconds** using native browser APIs.

---

## Architecture

```
simulator.py          →     data/alerts.csv     →     backend/app.py     →     frontend/index.html
(Log Generation)            (Shared Datastore)        (Correlation API)         (Dashboard UI)
```

---

## Tech Stack

- **Frontend** — Vanilla HTML5, CSS3 (glassmorphism dark-mode), JavaScript
- **Backend** — Python 3 + Flask REST API
- **Data** — Flat-file CSV (no database dependency)
- **Log Dialects** — Cisco IOS, Juniper Junos

---

## Dashboard

<div align="center">

![SSHlert Dashboard](assets/db_img.png)
<div align="center">
  Because your network deserves better than 3am pages for the same flap — twice
</div>
</div>

---

  <div align="center">

Built with ❤️ by tech9ic

</div>
