# Recommendation-AI

Recommendation-AI is a machine learning–powered API built with **Flask**, **scikit-learn**, and **pandas**.  
It provides intelligent product recommendations based on keywords, and also includes **speech-to-text integration** for real-time interaction.

---

## 🚀 Features
- Keyword-based recommendation API
- Speech-to-text input support
- Flask REST API endpoints
- Extensible for MySQL database integration
- Cross-Origin Resource Sharing (CORS) enabled

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/recommendation-ai.git
cd recommendation-ai
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
```

### 3. Activate the environment
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip3 install -r requirements.txt
```

### Install flusk and cors:
```bash
pip3 install pandas scikit-learn flask flask-cors
```

### Optional for MySQL:
```bash
pip3 install mysql-connector-python
```

### Optional for Speech-to-Text:
```bash
brew install portaudio
pip3 install SpeechRecognition pyaudio
```


## ▶️ Usage
Start the API
```bash
python3 app.py
```

### Run the generator script
```bash
python3 generate.py
```

## 🌐 API Endpoints

### Keyword-based recommendation
```bash
GET http://127.0.0.1:5000/recommend?keyword=Toyota
```

### Speech-to-text recording
```bash
GET http://127.0.0.1:5000/record?phrase_time_limit=2
```

## ⚙️ Utilities

### Kill a process running on port 5000
```bash
npx kill-port 5000
```

### Check SSL version
```bash
python3 -c "import ssl; print(ssl.OPENSSL_VERSION)"
```

### Ignore Python warnings
```bash
export PYTHONWARNINGS="ignore"
```

## 📌 Notes

Ensure Python 3.8+ is installed.

For macOS users, pyaudio may require additional build options:
```bash
pip3 install --global-option='build_ext' \
             --global-option='-I/usr/local/include' \
             --global-option='-L/usr/local/lib' pyaudio
```

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to change.

## 📄 License
This project is licensed under the MIT License.
