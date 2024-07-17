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

# for speech to text install
# brew install portaudio
# pip3 install SpeechRecognition pyaudio
# pip3 install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio

python generate.py
python app.py

http://127.0.0.1:5000/recommend?keyword=Toyota
