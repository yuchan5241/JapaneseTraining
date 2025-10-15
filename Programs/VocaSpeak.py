import requests
import numpy as np
import json
import sounddevice as sd


host = "127.0.0.1"
port = "50021"
speaker = 3

def post_audio_query(text: str) -> dict:
    params = {"text": text, "speaker": speaker}

    res = requests.post(
        f"http://{host}:{port}/audio_query",
        params=params,
    )

    query_data = res.json()

    return query_data

def post_synthesis(query_data: dict) -> bytes:
    params = {"speaker": speaker}
    headers = {"content-type": "application/json"}

    res = requests.post(
        f"http://{host}:{port}/synthesis",
        data = json.dumps(query_data),
        params=params,
        headers=headers,
    )

    return res.content

def play_wavfile(wav_data: bytes):
    sample_rate = 24000
    wav_array = np.frombuffer(wav_data, dtype=np.int16)
    sd.play(wav_array, sample_rate, blocking=True)

def text_to_voice():
    while True:
        text = input("입력 : ")
        if text == "q":
            exit()
        
        res = post_audio_query(text)
        wav = post_synthesis(res)
        play_wavfile(wav)


if __name__ == "__main__":
    text_to_voice()
