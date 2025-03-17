do_desyati = ['', 'один', 'два', 'три', 'четыре', 'пять',
              'шесть', 'семь', 'восемь', 'девять']

do_dvadtsayti = ['', 'одиннадцать', 'двенадцать', 'тринадцать',
                 'четырнадцать', 'пятнадцать', 'шестнадцать',
                 'семнадцать', 'восемнадцать', 'девятнадцать']

desyatki = ['', 'десять', 'двадцать', 'тридцать', 'сорок',
            'пятьдесят', 'шестьдесят', 'семьдесят',
            'восемьдесят', 'девяносто']


def nuber_to_words(n):
    if 10 < n < 20:
        return do_dvadtsayti[n - 10]

    ones_word = do_desyati[n % 10]
    tens_word = desyatki[n // 10]

    return (tens_word + ' ' + ones_word).strip()


n = int(input("Input number"))
print(nuber_to_words(n))
