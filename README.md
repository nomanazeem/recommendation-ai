# recommendation-ai
recommendation-ai

# Create an environment
python3 -m venv venv

# Activate the environment
source .venv/bin/activate

pip3 install pandas
pip3 install pandas scikit-learn
pip3 install flask       
#pip3 install Flask mysql-connector-python pandas scikit-learn

pip3 install flask-cors



# for speech to text install
# brew install portaudio
# pip3 install SpeechRecognition pyaudio
# pip3 install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio

# Check ssl version
# python3 -c "import ssl; print(ssl.OPENSSL_VERSION)"
# Ignore pyhton warning
# export PYTHONWARNINGS="ignore"

# My sql
# pip3 install mysql-connector-python
python generate.py

# kill port 
# npx kill-port 5000

python3 app.py

http://127.0.0.1:5000/recommend?keyword=Toyota


http://127.0.0.1:5000/record?phrase_time_limit=2
