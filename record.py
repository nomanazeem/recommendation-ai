from flask import Blueprint, jsonify, request
import speech_recognition as sr
import warnings

warnings.filterwarnings("ignore")
record_blueprint = Blueprint('record', __name__)

def record_speech(phrase_time_limit):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio_data = recognizer.listen(source, timeout=0, phrase_time_limit=phrase_time_limit)
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


@record_blueprint.route('/record', methods=['GET'])
def record():
    try:
        phrase_time_limit = int(request.args.get('phrase_time_limit', 2))

        if not phrase_time_limit:
            return jsonify({"error": "phrase_time_limit parameter is required"}), 400

        result = record_speech(phrase_time_limit)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500