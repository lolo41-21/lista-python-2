maiorIndice = -1
menorIndice = float('inf')
cidadeMaior = cidadeMenor = 0

somaVeiculos = 0
somaAcidentesPequenas = 0
contPequenas = 0

for i in range(5):
    print(f"\nCidade {i+1}:")
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Número de veículos de passeio (em 1999): "))
    acidentes = int(input("Número de acidentes com vítimas (em 1999): "))

    somaVeiculos += veiculos

    if acidentes > maiorIndice:
        maiorIndice = acidentes
        cidadeMaior = codigo
    if acidentes < menorIndice:
        menorIndice = acidentes
        cidadeMenor = codigo

    if veiculos < 2000:
        somaAcidentesPequenas += acidentes
        contPequenas += 1

mediaVeiculos = somaVeiculos / 5
mediaAcidentesPequenas = somaAcidentesPequenas / contPequenas if contPequenas > 0 else 0

print("--- Resultados ---")
print(f"maior número de acidentes: {maiorIndice} (Cidade {cidadeMaior})")
print(f"menor número de acidentes: {menorIndice} (Cidade {cidadeMenor})")
print(f"media de veículos nas 5 cidades: {mediaVeiculos:.2f}")
print(f"media de acidentes nas cidades com menos de 2000 veículos: {mediaAcidentesPequenas:.2f}")
