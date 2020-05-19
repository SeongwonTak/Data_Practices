def word_add():
    isalpha_check = False
    f = open("hangmanword.txt", 'a')
    print("Input new words for hangman")
    while isalpha_check == False:
        data = (input())
        isalpha_check = data.isalpha()
        if isalpha_check == False:
            print("Invalid inputs. Try again.")
    f.write(data)
    f.write('\n')
    f.close()

def word_view():
    f = open("hangmanword.txt", 'r')
    data = f.readlines()
    print('You have %d Words' % len(data))
    print('Enter your desired line to see the word')
    num = int(input())
    print(data[num-1])
    f.close()

def main():
    word_code = 0
    while word_code != 3:
        word_code = 0
        print('Word Editor')
        print('Choose the menu')
        print('1. Input Words')
        print('2. Check Words')
        print('3. Exit the Editor')
        while word_code not in range(1, 4):
            print('Enter your desired menu')
            try:
                word_code = int(input())
            except ValueError:
                print("Invalid inputs, try again")
                pass
        if word_code == 1:
            word_add()
        if word_code == 2:
            word_view()
        if word_code == 3:
            print("Back to the main")
if __name__ == '__main__':
    main()