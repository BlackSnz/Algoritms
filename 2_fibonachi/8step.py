def fib_mod(n, m):
    f0 = 0
    f1 = 1
    pizano = 1
    # Вычисление n-го числа Фибоначи
    
    # Вычисление периода Пизано для модуля m   
    f0, f1 = f1, f0+f1     
    while True:
        if f1 % m == 1 and f0 % m == 0:
            f0, f1 = f0, f1-f0
            break          
        f0, f1 = f1, f0+f1
        pizano += 1
        
    # Нахождение остатка от деления n-го числа Фибонначи на m
    print(fib(n % pizano))
    return n % pizano

# ГДЕ-ТО ТУТ ЕБЕТ МОЗГИ С n=0,1
def fib(n):
    f0 = 0
    f1 = 1
    for i in range(0, n + 1):
        if i > 2:
            f_n = (f0 + f1) % 10
            f0 = f1 % 10
            f1 = f_n % 10
        elif i == 1:
            f_n = 1
        else:
            f_n = 0
    return f_n 

for i in range (0, 18):
    fib_mod(i, 4)

   