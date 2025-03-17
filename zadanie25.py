def solve(*coefficients):
    # Проверка на допустимое количество коэффициентов
    if len(coefficients) not in {1, 2, 3}:
        return None

    # Инициализация коэффициентов a, b, c
    a, b, c = 0, 0, 0
    if len(coefficients) == 3:
        a, b, c = coefficients
    elif len(coefficients) == 2:
        b, c = coefficients
    else:
        c = coefficients[0]

    # Случай a = b = c = 0: бесконечное число решений
    if a == 0 and b == 0 and c == 0:
        return ["all"]

    # Решение квадратного уравнения (a != 0)
    if a != 0:
        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            return []
        elif discriminant == 0:
            x = (-b) / (2 * a)
            return [x]
        else:
            sqrt_d = discriminant**0.5
            x1 = (-b + sqrt_d) / (2 * a)
            x2 = (-b - sqrt_d) / (2 * a)
            return sorted([x1, x2])

    # Решение линейного уравнения (a = 0, но уравнение bx + c = 0)
    else:
        # Случай b = 0 (уравнение вырождается в c = 0)
        if b == 0:
            if c == 0:
                return ["all"]  # 0 = 0 → все решения
            else:
                return []       # c ≠ 0 → нет решений
        else:
            x = (-c) / b
            return [x]


print(solve(0, 0, 0))
print(solve(0, 0, 5))
print(solve(0, 2, 4))
print(solve(1, -3, 2))
print(solve(1, 2, 1))
print(solve(5))
