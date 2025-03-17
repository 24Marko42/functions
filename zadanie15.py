fractal = [0, None, None, 2]

# Заменяем элементы с индексами 1 и 2 на сам список fractal
# Это создает рекурсивную структуру, где fractal содержит сам себя
fractal[1] = fractal  # Теперь fractal[1] и fractal[2] указывает на fractal
fractal[2] = fractal
print(fractal)

# Можно использовать extend для добавления содержимого другого списка в текущий
fractal1 = []
fractal1.extend([0, fractal, fractal, 2])
print(fractal1)
