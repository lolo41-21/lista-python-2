linhas = int(input("digite o número de linhas da matriz: "))
colunas = int(input("digite o número de colunas da matriz: "))

matriz = []

print ("\ndigite os elementos da matriz: ")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

elementoProcurado = int(input("\ndigite o elemento que deseja contar: "))

contador = 0
for linha in matriz:
    contador += linha.count(elementoProcurado)

print ("\nMatriz digitada:")
for linha in matriz:
    print (linha)

print (f"\nO elemento {elementoProcurado} aparece {contador} vez(es) na matriz.")
