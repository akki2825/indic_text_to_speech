import glob
import logging
import indic_text_to_speech
from indic_text_to_speech import reader
from indic_text_to_speech.sound_lib import Library

speech_generator = indic_text_to_speech.SpeechGenerator(library=Library(path="/home/akhilesh/personal/indic_sound_library_voice_male_vv/"))

sentences = reader.from_plain_text("वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ")
print(sentences)
speech_generator.get_audio_for_sentence(sentences[0])
