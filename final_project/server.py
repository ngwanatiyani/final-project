from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    text = request.form.get('textToAnalyze')
    if not text:
        return "Invalid input! Please provide text to analyze.", 400
    result = emotion_detector(text)
    if result is None or result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    response = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
