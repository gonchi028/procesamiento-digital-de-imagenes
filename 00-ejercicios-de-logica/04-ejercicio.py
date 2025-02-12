def esPalindromo(palabra):
  inverso = ""
  for letra in palabra:
    inverso = letra + inverso
  return inverso == palabra

cadena = input("Introduce una cadena de texto: ")

if (esPalindromo(cadena)):
  print("La cadena es un palíndromo")
else:
  print("La cadena no es un palíndromo")
