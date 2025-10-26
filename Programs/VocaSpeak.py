import requests
import numpy as np
import json
import scipy.io.wavfile as wa
import re

host = "127.0.0.1"
port = "50021"
speaker = 3

VocaLen = int()

with open("Programs/JapaneseVoca.txt", "r", encoding="UTF-8") as f:
    VocaLen = len(f.readlines())

def post_audio_query(text: str) -> dict:  #function annoation :, -> 데이터의 타입에 대한 보충 설명, : (입력 데이터 타입), -> (출력 데이터 타입)
    params = {"text": text, "speaker": speaker}
    try:
        res = requests.post(
            f"http://{host}:{port}/audio_query",
            params=params,
        )
    except:
        print("웹 서버와 연결되지 않았습니다.")
        exit()
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

def play_wavfile(wav_data: bytes, text):
    sample_rate = 24000
    wav_array = np.frombuffer(wav_data, dtype=np.int16)
    wa.write(f"Programs/JapaneseVocaSound/{text}.wav", sample_rate, wav_array)  #발음 음성 파일 저장하는 코드



def text_to_voice(text: str):
    res = post_audio_query(text)
    wav = post_synthesis(res)
    play_wavfile(wav, text)


def texts_to_voice():
    with open("Programs/JapaneseVoca.txt", "r", encoding = "UTF-8") as f:
        Vocalist = f.readlines()
        Vocalist2 = list()
        for i in range(VocaLen):
            Vocalist2.append(re.split(r"[\u3000\s+]", Vocalist[i])[0])
    
    return Vocalist2

if __name__ == "__main__":

    txts = texts_to_voice()

    try:
        for i in range(VocaLen):
            text_to_voice(txts[i])
            print(f"음성파일 합성 중 {i+1}/{VocaLen}")
    except:
        print("합성 종료")