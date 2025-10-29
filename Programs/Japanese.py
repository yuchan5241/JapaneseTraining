import re
import random
import sounddevice as sd
import json
from scipy.io import wavfile

random_num = 0
already_answered = []
try_num = 0
try_string = str()
JF = open('Programs/JapaneseVoca.txt', 'r', encoding="UTF-8") # 상대 경로
Jstr = list()

with open("Programs/try_num.txt", 'r', encoding="UTF-8") as f:
    #try_num을 try_file에 저장된 시도 횟수를 읽어 저장
    try_string = f.readline()
    #파일에서 시도 횟수 가져오고 파일 닫기


#읽기 쓰기 타입으로 파일 염, 기존 내용 유지, 상대 경로로 열기
with open("Programs/try_num.txt", 'r+', encoding="UTF-8") as f:
    try_num = int(try_string) + 1
    f.write(f"{try_num}")
#파일 시도 횟수 저장하기



#시도 횟수 파일에 새로 쓰기

false_answer = open(f"Programs/false_answers/false_answer{try_num}.txt", 'w', encoding="UTF-8") # 상대 경로


print("프로그램을 종료하려면 exit를 입력하세요\n")

Jstr = JF.readlines()
Jstr2 = list()
    
while True:

    random_num = random.randint(0, len(Jstr))
    while random_num in already_answered:
        random_num = random.randint(0, len(Jstr))       # 일본어 중복시 다시 번호 뽑음
    
    already_answered.insert(0, random_num)      # 이미 뽑은 번호는 리스트에 추가
    Jstr2 = re.split(r"[\u3000\s+]", Jstr[random_num])
             
    print(f"한자 : {Jstr2[0]}\n")

    try:
        ans = input("발음 : ")
    except:
        break

    rate, wav_array = wavfile.read(f"Programs/JapaneseVocaSound/{Jstr2[0]}.wav")   #한자로 저장되어 있으므로 Jstr[0] 사용

    if(ans == "exit"):
        break
    if(ans == Jstr2[1]):
        print("맞았습니다.")
        sd.play(wav_array, samplerate=rate)
    else:
        print("틀렸습니다.")
        sd.play(wav_array, samplerate=rate)
        false_answer.write(f"{Jstr2[0]} {Jstr2[1]} {Jstr2[2]}\n")
    print()


false_answer.close()

JF.close()


#git init
#git add 파일명
#git commit -m "메모 내용"
#git log --all --oneline 저장 내용 보기
