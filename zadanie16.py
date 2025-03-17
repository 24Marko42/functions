def continue_fibonacci_sequence(sequence, n):
    # Ошибка: создание нового списка вместо модификации исходного
    for _ in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)  # Добавляем элемент в исходный список


sequence = [1, 1]
continue_fibonacci_sequence(sequence, 1)
print(*sequence)


sequence = [1, 1, 2, 3, 5]
continue_fibonacci_sequence(sequence, 0)
print(*sequence)
