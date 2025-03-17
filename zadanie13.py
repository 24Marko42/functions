numbers = ['1', '3', '4', '2']
print(numbers, id(numbers))
numbers.sort()
print(numbers, id(numbers))

numbers2 = ['1', '3', '4', '2']
numbers3 = sorted(numbers2)
print(numbers2, id(numbers2))
print(numbers3, id(numbers3))

"""айди нужны для отслеживания процессов и проверки на их совпадение, хотя тут и так
вроде понятно"""
