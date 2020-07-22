import glob
import logging
import indic_text_to_speech
from indic_text_to_speech import reader
from indic_text_to_speech.sound_lib import Library

speech_generator = indic_text_to_speech.SpeechGenerator(library=Library(path="/home/akhilesh/personal/indic_sound_library_voice_male_vv/"))

sentences = reader.from_plain_text(file_path="/home/akhilesh/personal/indic_text_to_speech/temp.txt")
speech_generator.get_audio_for_sentences(sentences=sentences, output_path="local/test.mp3")
