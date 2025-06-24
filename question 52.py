n = int(input("digite a ordem da matriz (n x n): "))

matriz = []
print ("\ndigite os elementos da matriz:")
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

somaPrincipal = 0
somaSecundaria = 0

for i in range(n):
    somaPrincipal += matriz[i][i]
    somaSecundaria += matriz[i][n - 1 - i]

print ("\nMatriz digitada:")
for linha in matriz:
    print (linha)

print (f"soma da diagonal principal: {somaPrincipal}")
print (f"soma da diagonal secundária: {somaSecundaria}")
