from flask import Flask, jsonify, request
from flask_cors import CORS
import speech_recognition as sr
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

def record_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio_data = recognizer.listen(source, timeout=0, phrase_time_limit=3)
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.WaitTimeoutError:
            return "No speech detected within the timeout period"
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results; {e}"
        except Exception as e:
            return str(e)

@app.route('/record', methods=['GET'])
def record():
    try:
        result = record_speech()
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
