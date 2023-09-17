import os

import speech_recognition as sr
from pydub import AudioSegment
from tqdm import tqdm

from logger import log


def transcribe_audio(audio_path, language='pt-BR'):
    """Transcribes the given audio file using Google Speech Recognition."""
    log.debug(f'transcribe_audio({audio_path}, language="pt-BR")')
    r = sr.Recognizer()

    # Split the audio into 30-second segments
    segment_duration = 30  # in seconds
    audio = AudioSegment.from_wav(audio_path)
    duration = len(audio) / 1000  # Total duration in seconds
    segments = int(duration / segment_duration)

    transcription = ""

    for i in tqdm(range(segments + 1), desc="Transcribing", unit="segment"):
        start_time = i * segment_duration * 1000
        end_time = (i + 1) * segment_duration * 1000
        audio_segment = audio[start_time:end_time]

        # Save the audio segment to a temporary file
        temp_filename = f"temp_segment_{i}.wav"
        log.debug(f'temp_filename: {temp_filename}')
        audio_segment.export(temp_filename, format="wav")

        with sr.AudioFile(temp_filename) as source:
            audio_data = r.record(source)
            try:
                text = r.recognize_google(audio_data, language=language)
                transcription += text + " "

            except sr.UnknownValueError:
                print(f"Segment {i + 1} not recognized.")
            except sr.RequestError as e:
                print(f"API request error on segment {i + 1}.")
                break  # Stop if there's an error calling the API

        # Remove the temporary file after using it
        os.remove(temp_filename)

    log.debug(f'transcription: {transcription}')
    return transcription.strip()
