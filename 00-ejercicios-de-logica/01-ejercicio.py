n = int(input("Ingrese un número: "))

fact = 1

for i in range(1, n+1):
  fact *= i

print(f"El factorial de {n} es {fact}")
