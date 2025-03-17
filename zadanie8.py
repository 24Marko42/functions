def tic_tac_toe(field):
    # Проверяем строки и столбцы
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] and field[i][0] != '-':
            return f"{field[i][0]} win"
        if field[0][i] == field[1][i] == field[2][i] and field[0][i] != '-':
            return f"{field[0][i]} win"

    # Проверяем диагонали
    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != '-':
        return f"{field[0][0]} win"
    if field[0][2] == field[1][1] == field[2][0] and field[0][2] != '-':
        return f"{field[0][2]} win"

    return "draw"


# Пример ввода поля в консоли:
data = """0 - 0
x x x
0 0 -"""

# Преобразуем строку в список списков (матрицу 3x3)
field = [line.split() for line in data.split('\n')]

# Вызываем функцию и печатаем результат
print(tic_tac_toe(field))
