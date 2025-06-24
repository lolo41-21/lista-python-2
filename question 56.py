linhas = int(input("digite o número de linhas: "))
colunas = int(input("digite o número de colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(i * j)
    matriz.append(linha)

print ("\nmatriz preenchida com o produto dos índices:")
for linha in matriz:
    print (linha)