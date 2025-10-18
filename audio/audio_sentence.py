from gtts import gTTS
import pathlib

def generate_sentence_audio(sentence, lang):
    tts = gTTS(sentence, lang=lang)
    tts.save(sentence + '.mp3')