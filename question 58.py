linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

matriz = []

print ("\nDigite os elementos da matriz:")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = input(f"Elemento [{i}][{j}]: ")
        linha.append(valor)
    matriz.append(linha)

matrizInvertida = matriz[::-1]

print ("\nMatriz original:")
for linha in matriz:
    print(linha)

print ("\nMatriz com linhas invertidas:")
for linha in matrizInvertida:
    print(linha)
