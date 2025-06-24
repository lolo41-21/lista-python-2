maiorAltura = menorAltura = 0
maisGordo = maisMagro = 0
codigoMaior = codigoMenor = codigoGordo = codigoMagro = 0

somaAlturas = somaPesos = 0
quantidade = 0

while True:
    codigo = int(input("digite o código do cliente (0 para encerrar): "))
    if codigo == 0:
        break

    altura = float(input("digite a altura (em metros): "))
    peso = float(input("digite o peso (em kg): "))

    if quantidade == 0:
        maiorAltura = menorAltura = altura
        maisGordo = maisMagro = peso
        codigoMaior = codigoMenor = codigoGordo = codigoMagro = codigo
    else:
        if altura > maiorAltura:
            maiorAltura = altura
            codigoMaior = codigo
        if altura < menorAltura:
            menorAltura = altura
            codigoMenor = codigo
        if peso > maisGordo:
            maisGordo = peso
            codigoGordo = codigo
        if peso < maisMagro:
            maisMagro = peso
            codigoMagro = codigo

    somaAlturas += altura
    somaPesos += peso
    quantidade += 1

if quantidade > 0:
    mediaAltura = somaAlturas / quantidade
    mediaPeso = somaPesos / quantidade

    print("--- Resultados do Censo ---")
    print(f"Cliente mais alto: Código {codigoMaior} com {maiorAltura} m")
    print(f"Cliente mais baixo: Código {codigoMenor} com {menorAltura} m")
    print(f"Cliente mais gordo: Código {codigoGordo} com {maisGordo} kg")
    print(f"Cliente mais magro: Código {codigoMagro} com {maisMagro} kg")
    print(f"Média das alturas: {mediaAltura} m")
    print(f"Média dos pesos: {mediaPeso:.2f} kg")