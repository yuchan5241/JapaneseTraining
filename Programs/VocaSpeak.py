import requests
import numpy as np
import json
import sounddevice as sd

host = "127.0.0.1"
port = "50021"
speaker = 3

def post_audio_query(text: str) -> dict:  #function annoation :, -> 데이터의 타입에 대한 보충 설명, : (입력 데이터 타입), -> (출력 데이터 타입)
    params = {"text": text, "speaker": speaker}

    res = requests.post(
        f"http://{host}:{port}/audio_query",
        params=params,
    )

    query_data = res.json()     #음성 합성을 위한 쿼리문(높낮이, 소리 크기, 말하기 속도 등의 데이터들이 json 파일 형태로 담겨있음)
                                #.json() 함수는 json 파일 내용을 딕셔너리 타입으로 바꿔준다.

    return query_data

def post_synthesis(query_data: dict) -> bytes:
    params = {"speaker": speaker}
    headers = {"content-type": "application/json"}

    res = requests.post(
        f"http://{host}:{port}/synthesis",
        data = json.dumps(query_data),     #json.dumps() 딕셔너리 타입의 내용을 json 타입으로 교체하는 함수
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
