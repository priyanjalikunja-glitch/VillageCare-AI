# 🌿 VillageCare AI

### Better Healthcare, Closer to Home

VillageCare AI is an AI-powered healthcare information assistant designed to help people in rural and village communities access simple, easy-to-understand health information.

The project uses Python, Flask, and Google Gemini AI to answer general health-related questions.

## 🎯 Problem Statement

Many rural communities face challenges accessing reliable healthcare information. VillageCare AI aims to make general health education more accessible through an easy-to-use web application.

## 💡 Features

- 🤖 **AI Health Assistant:** Answers general health questions using Google Gemini AI.
- 🌿 **Simple Interface:** Clean and user-friendly website.
- 🏥 **Health Education:** Provides general information about health and wellness.
- 🌐 **Web-Based Application:** Accessible through a web browser.
- 📱 **Responsive Design:** Designed to work across different screen sizes.

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Google Gemini API
- python-dotenv

## 📁 Project Structure

```text
VillageCare-AI/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/VillageCare-AI.git
cd VillageCare-AI
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root directory and add your Google Gemini API key:

```dotenv
GEMINI_API_KEY=your_api_key_here
```

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Security:** Never upload your `.env` file or API key to GitHub.

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🔒 Healthcare Disclaimer

VillageCare AI provides general health education and is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for personal medical concerns. Seek emergency care immediately when needed.

## 🚀 Future Improvements

- Support for more Indian languages.
- Information about nearby healthcare facilities.
- Voice-based health questions.
- Health awareness resources for rural communities.
- Improved accessibility for users with limited digital experience.

## 🤝 Contributing

Suggestions and contributions to improve VillageCare AI are welcome.

## 📄 License

This project is available for educational and learning purposes. A formal open-source license can be added when one is selected.
