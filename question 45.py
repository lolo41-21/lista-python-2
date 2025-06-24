print ("digite o gabarito da prova (10 questões):")
gabarito = []
for i in range(1, 11):
    resposta = input(f"Resposta da questão {i}: ").strip()
    gabarito.append(resposta)

maiorAcerto = -1
menorAcerto = 11
totalAlunos = 0
somaNotas = 0

while True:
    print("\nAluno, responda a prova:")
    acertos = 0
    for i in range(10):
        respostaAluno = input(f"Questão {i+1}: ").strip()
        if respostaAluno == gabarito[i]:
            acertos += 1

    print(f"Total de acertos: {acertos}")
    print(f"Nota: {acertos} ponto(s)")

    if acertos > maiorAcerto:
        maiorAcerto = acertos
    if acertos < menorAcerto:
        menorAcerto = acertos

    totalAlunos += 1
    somaNotas += acertos

    outro = input("Outro aluno vai usar o sistema? (s/n): ").strip()
    if outro != 's':
        break

if totalAlunos > 0:
    mediaNotas = somaNotas / totalAlunos
    print ("\nResultados")
    print (f"Maior acerto: {maiorAcerto}")
    print (f"Menor acerto: {menorAcerto}")
    print (f"Total de alunos: {totalAlunos}")
    print (f"Média das notas: {mediaNotas:.2f}")

