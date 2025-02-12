numeros = {}

for i in range(7):
  num = int(input(f"Ingrese el número {i + 1}: "))
  numeros[num] = numeros.get(num, 0) + 1

numMax = 0
cantMax = 0

first = True

for num, cant in numeros.items():
  if first:
    numMax = num
    cantMax = cant
    first = False
  elif cant > cantMax:
    numMax = num
    cantMax = cant

print(f"El número que más veces se repite es {numMax} con {cantMax} repeticiones")
