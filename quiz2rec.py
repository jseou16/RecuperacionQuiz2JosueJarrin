while True: 
    try:
        cantidad = int(input("Cuantos numeros quiere ordenar? "))
    except ValueError:
        print("Error! ingrese un numero ")
    else: 
        break

numeros = []

for i in range(cantidad): 
    try: 
        numero = float(input(f"Escriba su numero #{i+1}: "))
        numeros.append(numero)
    except ValueError:
        print("Error! ingrese solo numeros")

listaDesorden = numeros.copy()

cuantosNumeros = len(numeros)

for k in range(cuantosNumeros):
    for j in range(0, cuantosNumeros - k - 1):
        if numeros[j] > numeros [j+1]:
            numeros[j],numeros[j+1] = numeros[j+1],numeros[j]

print(f"Lista sin ordenar nada: {listaDesorden}")
print(f"Lista ya ordenada: {numeros}")
