while True:
    nomeAtleta = input("Atleta: ")
    if nomeAtleta.strip() == "":
        break

    notas = []
    for i in range(7):
        nota = float(input("Nota: "))
        notas.append(nota)

    print(f"\nAtleta: {nomeAtleta}")
    for nota in notas:
        print(f"Nota: {nota:.1f}")

    melhorNota = max(notas)
    piorNota = min(notas)

    notasRestantes = notas.copy()
    notasRestantes.remove(melhorNota)
    notasRestantes.remove(piorNota)

    calculoMedia = sum(notasRestantes) / len(notasRestantes)

    print ("\nResultado final:")
    print (f"Atleta: {nomeAtleta}")
    print (f"Melhor nota: {melhorNota:.1f}")
    print (f"Pior nota: {piorNota:.1f}")
    print (f"Média: {calculoMedia:.2f}\n")
