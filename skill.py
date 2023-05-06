def greeting():
    print("Это игра крестики-нолики")
    print("формат ввода: х, у")
    print("х - номер строки, у - номер слолбца")

def show():
    print("    | 0 | 1 | 2 | ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
    print()

def ask():
    while True:
        cords = input("    Ваш ход: ").split()
        if len(cords) != 2:
            print("Введите 2 координаты")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2 :
            print("Координаты вне диапазона")
            continue

        return x, y

def check_win():
    win_cord =  (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]] [c[1]])
        if symbols == ["x", "x", "x"]:
            print("x выиграл")
            return True
        if symbols == ["o", "o", "o"]:
            print("o выиграл")
            return True
    return False

greeting()
field = [[" "] * 3 for i in range(3) ]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("ходит Х")
    else:
        print("ходит О")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "o"

    if check_win():
        break

    if count == 9:
        print("ничья")
        break