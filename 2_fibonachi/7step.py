# Нахождение последний цифры большого числа Фибоначчи  

import time
start_time = time.time()
def fib(n):
    f0 = 0
    f1 = 1
    for i in range(0, n + 1):
        if i > 1:
            f_n = (f0 + f1) % 10
            f0 = f1 % 10
            f1 = f_n % 10
        else: f_n = 0 
    
    return f_n
print(fib(841645))
print(f'{time.time()-start_time} second')
