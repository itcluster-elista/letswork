var_1 = int(input("Введите число: "))
count = 0
while var_1 > 0:
    count = count + 1
    var_1 = var_1 // 10
print("Количество цифр равно:", count)


var_1 = int(input("Введите число: "))
total = 0
while var_1 > 0:
    rest = var_1 % 10
    total = total + rest
    var_1 = var_1//10
print("Сумма цифр равна:", total)

