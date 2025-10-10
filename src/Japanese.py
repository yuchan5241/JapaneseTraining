import re
import random

random_num = 0
already_answered = []
try_num = 0
try_string = str()
JF = open('C:/Japanese/src/JapaneseVoca.txt', 'r', encoding="UTF-8")
Jstr = list()
try_file = open("C:/Japanese/src/try_num.txt", 'r', encoding="UTF-8")


#try_num을 try_file에 저장된 시도 횟수를 읽어 저장
try_string = try_file.readline()
try_file.close()
#파일에서 시도 횟수 가져오고 파일 닫기

try_file = open("C:/Japanese/src/try_num.txt", 'r+', encoding="UTF-8") #읽기 쓰기 타입으로 파일 염, 기존 내용 유지

try_num = int(try_string) + 1
try_file.write(f"{try_num}")

#파일 시도 횟수 저장하기

try_file.close()

#시도 횟수 파일에 새로 쓰기

false_answer = open(f"C:/Japanese/src/false_answers/false_answer{try_num}.txt", 'w', encoding="UTF-8")


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

    if(ans == "exit"):
        break
    if(ans == Jstr2[1]):
        print("맞았습니다.")
    else:
        print("틀렸습니다.")
        false_answer.write(f"{Jstr2[0]} {Jstr2[1]} {Jstr2[2]}\n")
    print()


false_answer.close()

JF.close()



# 일본어 프로그램
# 단어는 랜덤
# 랜덤으로 만드는 방법
# readlines로 한줄 한줄을 리스트로 만든 후, 랜덤 모듈로 숫자를 가져와서 split으로 나눈다.
# 반복 횟수는 단어 갯수만큼

#C:\Users\sunfl\AppData\Local\Programs\VOICEVOX\vv-engine voicevox 사이트 연결 exe'
#git init
#git add 파일명
#git commit -m "메모 내용"
#git log --all --oneline 저장 내용 보기
