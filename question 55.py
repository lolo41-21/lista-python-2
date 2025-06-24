linhas = int(input("digite o número de linhas da matriz: "))
colunas = int(input("digite o número de colunas da matriz: "))

matriz = []
print ("\ndigite os elementos da matriz:")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = float(input(f"elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

maior = matriz[0][0]
menor = matriz[0][0]

for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

print (f"\nMaior elemento da matriz: {maior}")
print (f"menor elemento da matriz: {menor}")
