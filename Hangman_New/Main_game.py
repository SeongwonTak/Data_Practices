import random

def wordgiven():
    f = open("hangmanword.txt", 'r')
    data = f.readlines()
    num = random.randrange(1 , len(data)+1) #파일 전체 중 하나 선택.
    return (data[num-1])
    f.close()

def main():
    answer = wordgiven() #이미 문자열로 인식 완료
    in_playing = []
    for i in range (0, len(answer)-1):
        in_playing.append("*")
    print('Choose the game level')
    print('1. Novice : 20 lives')
    print('2. Easy : 12 lives')
    print('3. Normal : 8 lives')
    print('4. Hard : 5 lives')
    print('5. Devilish : 1 life')

    level: int = 0
    life_list = [20, 12, 8, 5, 1]
    while level not in range(1, 6):
        print('Enter your desired level')
        try:
            level = int(input())
        except ValueError:
            print("Invalid inputs, try again")
            pass

    life = life_list[level-1]

    while True:
        char_judge = 0
        counter = 0
        isalpha_check = False
        print(in_playing)
        print("Life : %d " % life)

        while isalpha_check == False:
            print("Enter your trial")
            check = (input()) #검사할 문자열을 입력받는다.
            isalpha_check = check.isalpha()
            if len(check) > 1: #두글자 이상 받으면, 비유효하므로 다시받는다.
                isalpha_check = False
            if isalpha_check == False:
                print("Invalid inputs. Try again.")

        for i in range(0, len(answer)-1):
            if check == answer[i]:
                in_playing[i] = check #입력글자 넣기. 수정이 필요해서 리스트
                char_judge = 1

        if char_judge == 0:  #위에서 하나라도 있으면 judge가 1이 됨
            print("There is no %c" % check)
            life -= 1

        if life == 0:
            print("Fail! Game over!")
            print(answer)
            break

        for i in range (0, len(answer)-1):#하나라도 *표면, 다 풀지 않아서 게임 속행
            if in_playing[i] != '*':
                counter += 1
        if len(answer) == counter + 1:
            print('You Win')
            print(answer)
            break

if __name__ == '__main__':
    main()