# Нахождение остатка от деления n-го числа Фибонначи на m
# Алгоритм основан на нахождении периода Пизано для модуля m


def fib_mod(n, m):
    f0 = 0
    f1 = 1
    pizano = 1
    
    
    # Вычисление периода Пизано для модуля m   
    f0, f1 = f1, f0+f1     
    while True:
        if f1 % m == 1 and f0 % m == 0:
            f0, f1 = f0, f1-f0
            break          
        f0, f1 = f1, f0+f1
        pizano += 1
        
    # Нахождение остатка от деления n-го числа Фибонначи на m
    if n <= pizano:
        print(f'Остаток от деления {n}-го числа Фибоначчи на {m}: {fib(n) % m}')
        return fib(n) % m
    else:
        print(f'Остаток от деления {n}-го числа Фибоначчи на {m}: {fib(n % pizano) % m}')
        return fib(n % pizano) % m

# Вычисление n-го числа Фибоначи
def fib(n):
    f0 = 0
    f1 = 1
    for i in range(0, n + 1):
        if i > 1:
            f_n = f0 + f1
            f0 = f1
            f1 = f_n
        elif i == 1: f_n = 1
        else: f_n = 0 
    return f_n

fib_mod(10, 4)

   