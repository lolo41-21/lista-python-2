linhas = int(input("Digite o número de linhas da matriz: "))
matriz = []

formato = True
numeroColunas = None

for i in range(linhas):
    linha = input(f"Digite os elementos da linha {i} separados por espaço: ")
    
    if numeroColunas is None:
        numeroColunas = len(linha)
    elif len(linha) != numeroColunas:
        formato = False  

    matriz.append(linha)

eQuadrada = formato and (linhas == numeroColunas)

print(eQuadrada)
