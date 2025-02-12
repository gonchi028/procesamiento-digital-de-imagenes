while True:
  n = int(input("Ingrese la cantidad de numeros que desea ingresar (no menor a 3): "))
  if n >= 3:
    break
  else:
    print("El numero ingresado es menor a 3")

for i in range (n):
  num = int(input(f"Ingrese el numero {i+1}: "))
  if i == 0:
    mayor = num
    menor = num
  else:
    if num > mayor:
      mayor = num
    if num < menor:
      menor = num

print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")
