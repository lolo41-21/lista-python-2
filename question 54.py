linhas = int(input("digite o número de linhas da matriz: "))
colunas = int(input("digite o número de colunas da matriz: "))

matriz = []
print ("\ndigite os elementos da matriz:")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

transposta = []
for j in range(colunas):
    novaLinha = []
    for i in range(linhas):
        novaLinha.append(matriz[i][j])
    transposta.append(novaLinha)

print ("\nmatriz original:")
for linha in matriz:
    print(linha)

print ("\nmatriz transposta:")
for linha in transposta:
    print (linha)