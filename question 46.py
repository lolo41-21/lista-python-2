while True:
    nomeAtleta = input("Nome do atleta: ")
    if nomeAtleta.strip() == "":
        break

    saltos = []
    ordens = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]

    for i in range(5):
        distancia = float(input(f"{ordens[i]} salto: "))
        saltos.append(distancia)

    print(f"\nAtleta: {nomeAtleta}")
    for i in range(5):
        print(f"{ordens[i]} Salto: {saltos[i]} m")

    melhorSalto = max(saltos)
    piorSalto = min(saltos)

    saltosRestantes = saltos.copy()
    saltosRestantes.remove(melhorSalto)
    saltosRestantes.remove(piorSalto)

    calculoMedia = sum(saltosRestantes) / len(saltosRestantes)

    print (f"\nMelhor salto: {melhorSalto} m")
    print (f"Pior salto: {piorSalto} m")
    print (f"Média dos demais saltos: {calculoMedia:.1f} m")
    print ("\nResultado final:")
    print (f"{nomeAtleta}: {calculoMedia:.1f} m\n")