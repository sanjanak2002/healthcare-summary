# speech_to_text.py

from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer
from config import get_azure_subscription_key

def transcribe_audio(audio_file_path, region):
    subscription_key = get_azure_subscription_key()
    speech_config = SpeechConfig(subscription=subscription_key, region=region)
    speech_recognizer = SpeechRecognizer(speech_config=speech_config)

    with open(audio_file_path, "rb") as audio_file:
        audio_data = audio_file.read()
        result = speech_recognizer.recognize_once(audio_data)

    if result.reason == ResultReason.RecognizedSpeech:
        return result.text
    else:
        return f"Speech recognition failed: {result.reason}"
