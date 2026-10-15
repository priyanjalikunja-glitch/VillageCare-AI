# 🏥 VillageCare AI

### AI-Powered Healthcare Information Assistant for Rural Communities

VillageCare AI is a web-based project designed to make general healthcare information more accessible to people in villages and communities. It combines an AI-powered assistant, multilingual interaction, voice features, and quick access to healthcare resources in one simple interface.

🌐 **Live Website:** https://village-care-ai.vercel.app/assistant

💻 **GitHub Repository:** https://github.com/priyanjalikunja-glitch/VillageCare-AI

---

## 📌 Problem Statement

People in rural and underserved communities may face difficulties accessing understandable healthcare information, finding nearby healthcare resources, and using digital health platforms because of language and accessibility barriers.

## 💡 Our Solution

VillageCare AI provides a simple web interface where users can explore healthcare-related information, ask general health questions, and access useful healthcare resources.

## ✨ Key Features

- 🤖 **AI Healthcare Assistant:** Ask general healthcare questions and receive AI-generated information.
- 🌐 **Multilingual Support:** Interact in English, Telugu, and Hindi.
- 🎤 **Voice Input:** Ask questions using speech where browser support is available.
- 🔊 **Voice Output:** Listen to the assistant's responses.
- 🏥 **Nearby Hospitals:** Quickly open Google Maps to find hospitals.
- 💊 **Medical Shops:** Open Google Maps to search for medical shops.
- 📚 **Health Awareness:** Access a dedicated section for health awareness information.
- 🩺 **Health Services:** Explore the healthcare services section.
- 📱 **Simple User Interface:** Navigate through separate sections using interactive menu cards.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| HTML | Web page structure |
| CSS | Styling and responsive layout |
| JavaScript | Interactive menu and voice features |
| Python | Backend programming |
| Flask | Web server and API routes |
| Google Gemini API | AI-generated responses |
| Web Speech API | Browser-based speech input and output |
| Google Maps | Finding nearby healthcare resources |
| Git and GitHub | Version control and source code |
| Vercel | Deployment |

## ⚙️ Run the Project Locally

### Prerequisites

- Python 3.11 or a compatible Python version
- Visual Studio Code
- A Google Gemini API key

### 1. Clone the repository

```bash
git clone https://github.com/priyanjalikunja-glitch/VillageCare-AI.git
cd VillageCare-AI
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root and add:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your own API key. Keep `.env` private and never upload your actual API key to GitHub.

### 5. Start the application

```bash
python app.py
```

Open the application in your browser:

http://127.0.0.1:5000/

To open the AI assistant directly:

http://127.0.0.1:5000/assistant

## 🩺 Healthcare Safety

VillageCare AI is intended for general healthcare information and awareness. It does not replace a qualified healthcare professional, medical diagnosis, or treatment.

- Do not use AI responses as a substitute for professional medical advice.
- Consult a qualified healthcare professional for medical concerns.
- In a serious emergency in India, call **112** or go to the nearest emergency department.

## 🚀 Future Improvements

- Add more regional languages.
- Improve mobile accessibility.
- Expand verified healthcare resource information.
- Add more health awareness materials.
- Improve error handling and accessibility testing.

## 🎯 Project Goal

The goal of VillageCare AI is to explore how artificial intelligence and accessible web technologies can help make general healthcare information easier to access for rural communities.

## 👩‍💻 Project Information

**Project Name:** VillageCare AI  
**Category:** Artificial Intelligence / Healthcare Technology  
**Backend:** Python and Flask  
**AI Integration:** Google Gemini API  
**Deployment:** Vercel

---

*Built with ❤️ to explore accessible healthcare information for rural communities.*
