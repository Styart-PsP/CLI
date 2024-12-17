import math

a_value = float(input("Введіть значення для a: "))
b_value = float(input("Введіть значення для b: "))

if a_value >= 15:
    result = math.sin(2*a_value)**2 + math.cos(2*b_value)**2
else:
    result = math.sqrt(a_value**2 + b_value**2)

print(f"Результат: {result}")