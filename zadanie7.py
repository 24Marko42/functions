def palindrome(s):
    # Убираем пробелы и знаки препинания (str.isalnum), приводим к нижнему регистру
    s = ''.join(filter(str.isalnum, s.lower()))
    return "Палиндром" if s == s[::-1] else "Не палиндром"


print(palindrome("Палиндром"))
print(palindrome("А роза упала на лапу Азора"))
