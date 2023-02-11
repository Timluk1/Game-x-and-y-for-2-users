import time

table = []


def begin_game():
    global table
    table = [["0"] * 3 for i in range(3)]


def begin():
    print("_____________________")
    print("  Game x and y")
    print("---------------------")
    print("Do you want to begin game? (Yes or No)")
    play = input()
    if play == "Yes":
        begin_game()
        show_table()
        game_user1()
    else:
        begin()


def show_table():
    print("Table now:")
    for i in table:
        print(*i)


def game_user1():
    global table
    x, y = map(int, input("Enter the row and column player X: ").split())
    if table[x - 1][y - 1] == "0":
        table[x - 1][y - 1] = "X"
        check_draw()
        victory_check()
    else:
        if table[x - 1][y - 1] == "X":
            print("Ты долбоеб ты туда уже X вьебал, еще пробуй....")
            game_user1()
        else:
            print("Ты еблан соперник уже Y вьебал туда, еще пробуй....")
            game_user1()
    show_table()
    game_user2()


def game_user2():
    x, y = map(int, input("Enter the row and column player Y: ").split())
    if table[x - 1][y - 1] == "0":
        table[x - 1][y - 1] = "Y"
        check_draw()
        victory_check()
    else:
        if table[x - 1][y - 1] == "X":
            print("Ты еблан соперник уже X вьебал туда, еще пробуй....")
            game_user2()
        else:
            print("Ты долбоеб ты туда уже Y вьебал, еще пробуй....")
            game_user2()
    show_table()
    game_user1()


def victory_check():
    for i in range(3):
        if "".join(table[i]).count("X") == 3:
            show_table()
            print("X win!!!")
            time.sleep(1)
            begin()
            break
        elif "".join(table[i]).count("Y") == 3:
            show_table()
            print("Y win!!!")
            time.sleep(1)
            begin()
            break
    index = 0
    for j in range(3):
        count_x = 0
        count_y = 0
        for i in range(3):
            if table[i][index] == "X":
                count_x += 1
            elif table[i][index] == "Y":
                count_y += 1
        if count_x == 3:
            show_table()
            print("X win!")
            time.sleep(1)
            begin()
        elif count_y == 3:
            show_table()
            print("Y win!")
            time.sleep(1)
            begin()
        index += 1
    count_x = 0
    count_y = 0
    for j in range(3):
        if table[j][j] == "X":
            count_x += 1
        elif table[j][j] == "Y":
            count_y += 1
    if count_x == 3:
        show_table()
        print("X win!!")
        time.sleep(1)
        begin()
    elif count_y == 3:
        show_table()
        print("Y win!!")
        time.sleep(1)
        begin()
    if table[0][2] + table[1][1] + table[2][0] == "XXX":
        show_table()
        print("X win!!!!")
        time.sleep(1)
        begin()
    if table[0][2] + table[1][1] + table[2][0] == "YYY":
        show_table()
        print("Y win!!!!!")
        time.sleep(1)
        begin()


def check_draw():
    if "0" not in table[0] and "0" not in table[1] and "0" not in table[2]:
        show_table()
        print("Ну вы и ебланы в ничью сыиграли")
        time.sleep(1)
        begin()


if __name__ == "__main__":
    begin()
