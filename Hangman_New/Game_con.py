import Main_game
import Word_edit

def main():
    menu_code = 0
    while menu_code != 3:
        menu_code = 0
        print('Hang Man ver 0.01')
        print('Choose the menu')
        print('1. Play game')
        print('2. Word Editor')
        print('3. Exit the game')
        while menu_code not in range(1, 4):
            print('Enter your desired menu')
            try:
                menu_code = int(input())
            except ValueError:
                print("Invalid inputs, try again")
                pass
        if menu_code == 1:
            Main_game.main()
        if menu_code == 2:
            Word_edit.main()
        if menu_code == 3:
            print("See you later")

if __name__ == '__main__':
    main()