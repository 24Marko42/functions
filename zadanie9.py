previous_message = None  # Глобальная переменная для хранения предыдущего сообщения


def print_without_duplicates(message):
    global previous_message
    if message != previous_message:
        print(message)
        previous_message = message


# Пример работы
print_without_duplicates("Привет")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Когда доедешь до дома")
print_without_duplicates("Ага, жду")
print_without_duplicates("Ага, жду")
