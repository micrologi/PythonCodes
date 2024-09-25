def factorial(n):
    if n == 1: # O caso base (condição de rescisão).
        return 1
    else:
        return n * factorial(n - 1)
 
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24