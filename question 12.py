numero = int(input("Digite um número entre 1 e 10 para ver tabuada: "))

if 1 <= numero <= 10:
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
else:
    print("Número inválido! Digite um número entre 1 e 10.")