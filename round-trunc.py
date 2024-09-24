import math

def truncar_decimal(num, casas):
    fator = 10 ** casas
    return math.trunc(num * fator) / fator


valor = 499.5499999999999

print(f"Numero com round: {round(valor,2)}.")
print(f"Numero com round: {valor:.2f}.")

print(f"Numero com trunc: {truncar_decimal(valor,2)}.")
