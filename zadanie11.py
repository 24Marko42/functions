# Глобальные переменные
one = 5
two = 4
three = 0


def int_to_roman(n):
    roman_numerals = [
        # опять кучу чисел добавлять в кортеж?...
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    result = ""
    for value, symbol in roman_numerals:
        while n >= value:
            result += symbol
            n -= value
    return result


def roman():
    global three
    three = one + two
    print(f"{int_to_roman(one)}+{int_to_roman(two)}={int_to_roman(three)}")


# Пример использования:
roman()  # Вывод: V+IV=IX
