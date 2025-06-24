maisAlto = maisBaixo = 0
codAlto = codBaixo = 0

for i in range(10):
    cod = int(input(f"Número do aluno {i+1}: "))
    altura = int(input("Altura (em cm): "))

    if i == 0:
        maisAlto = maisBaixo = altura
        codAlto = codBaixo = cod
    else:
        if altura > maisAlto:
            maisAlto = altura
            codAlto = cod
        if altura < maisBaixo:
            maisBaixo = altura
            codBaixo = cod

print(f"Aluno mais alto: Nº {codAlto} com {maisAlto} cm")
print(f"Aluno mais baixo: Nº {codBaixo} com {maisBaixo} cm")
