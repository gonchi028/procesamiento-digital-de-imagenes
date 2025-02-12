def ordenarBurbuja(arreglo):
  n = len(arreglo)
  for i in range(n - 1):
    for j in range(n - 1 - i):
      if arreglo[j] > arreglo[j+1]:
        arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

arreglo = [64, 34, 25, 12, 22, 11, 90]
ordenarBurbuja(arreglo)
print(arreglo)
