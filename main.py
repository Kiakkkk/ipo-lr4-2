print("Введите список чисел: ")
x = [int(input()) for i in range(5)] #вводятся числа с клавиатуры
x = [x[i]**2 for i in range(0, 5)]
print(f"{x}", end=" ")