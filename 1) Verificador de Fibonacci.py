def fibonacci_checker(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return f"{num} pertence à sequência de Fibonacci."
    else:
        return f"{num} não pertence à sequência de Fibonacci."

# Número a ser verificado
numero = 21

print(fibonacci_checker(numero))