# 🤖 JARVIS AI Assistant v1.0

A futuristic AI-powered desktop assistant inspired by Iron Man's JARVIS.

Built using Python, Ollama AI, Speech Recognition, Text-to-Speech, Desktop Automation, and a custom Dashboard UI.

---

# 🚀 Features

### 🎤 Voice Interaction

* Real-time speech recognition
* Natural voice commands
* Wake-and-respond workflow

### 🧠 AI Integration

* Ollama Local AI
* Qwen 2.5 Model
* Offline AI conversations
* Intelligent responses

### 🔊 Voice Output

* Text-to-Speech responses
* Real-time spoken replies
* Voice feedback system

### 🌐 Automation

* Open YouTube
* Open Google
* Open ChatGPT
* Search Weather
* Music Search

### 📊 Dashboard

* Live Assistant Status
* Interactive GUI
* Arc-Reactor Inspired Interface
* Real-Time Updates

### 💻 System Monitoring

* CPU Usage Monitoring
* RAM Usage Monitoring
* System Information

---

# 🏗 Architecture

User Voice Input
↓
Speech Recognition
↓
Brain Engine
↓
Predefined Commands / Ollama AI
↓
Response Engine
↓
Text To Speech
↓
User Output

---

# 📂 Project Structure

```text
jarvis/
│
├── main.py
├── README.md
├── requirements.txt
│
├── core/
│   ├── brain.py
│   └── processor.py
│
├── voice/
│   ├── listen.py
│   ├── speak.py
│   └── state.py
│
├── gui/
│   ├── dashboard.py
│   └── reactor.py
│
├── modules/
│   └── system_monitor.py
│
└── config/
    └── settings.py
```

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/seebee123/My-Jarvis.git
cd My-Jarvis
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Start Ollama

```bash
ollama serve
```

### Run Jarvis

```bash
python main.py
```

---

# 🎯 Supported Commands

### Basic Commands

* hello
* your name
* time
* joke
* coin toss
* roll dice

### Automation

* open youtube
* open google
* open chatgpt
* weather
* play music

### Control

* exit
* quit
* shutdown

### AI Mode

Any unknown command automatically goes to Ollama AI.

---

# 🛠 Technologies Used

* Python
* Ollama
* Qwen 2.5
* SpeechRecognition
* pyttsx3
* PyQt
* psutil
* threading

---

# 📈 Current Version

```text
Jarvis v1.0 Stable Release
```

Status:

* Voice Recognition ✅
* Voice Output ✅
* Ollama AI ✅
* Dashboard ✅
* Automation ✅
* GitHub Integration ✅

---

# 👨‍💻 Developer

Seebee Koundal

---

# 🏆 Project Goal

To create a personal AI desktop assistant capable of voice interaction, local AI reasoning, desktop automation, and future expansion into a complete Iron-Man-style JARVIS ecosystem.
