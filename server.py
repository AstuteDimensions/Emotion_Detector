"""
Server module for Emotion Detection Flask application.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the home page.
    """
    return "Emotion Detection App is running!"


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle emotion detection requests and return formatted response.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Handle blank input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
