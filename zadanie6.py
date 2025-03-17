def bracket_check(test_string):
    sravnenie = []
    for simvol in test_string:
        if simvol == '(':
            sravnenie.append('(')
        elif simvol == ')':
            if not sravnenie or sravnenie[-1] != '(':
                return 'NO'
            sravnenie.pop()
    return 'YES' if not sravnenie else 'NO'


print(bracket_check("()"))       # Выведет: YES
print(bracket_check("(()(("))    # Выведет: NO

# test_string = str(input("Input string of ( or ):"))
# print(bracket_check(test_string))
