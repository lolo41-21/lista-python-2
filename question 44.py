candidatos = {1: "José", 2: "João", 3: "Maria", 4: "Ana"}
votos = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

print("candidatos:")
for c, n in candidatos.items():
    print(f"{c} - {n}")
print("5 - Voto Nulo")
print("6 - Voto em Branco")

while True:
    voto = int(input("digite o código do voto (0 para sair): "))
    if voto == 0:
        break
    if voto in votos:
        votos[voto] += 1
    else:
        print("código inválido.")

totalVotos = sum(votos.values())
percentNulos = (votos[5] / totalVotos * 100) if totalVotos > 0 else 0
percentBrancos = (votos[6] / totalVotos * 100) if totalVotos > 0 else 0

print("\nResultado:")
for c, n in candidatos.items():
    print(f"{n}: {votos[c]} votos")
print (f"Votos Nulos: {votos[5]}")
print (f"Votos em Branco: {votos[6]}")
print (f"% votos nulos: {percentNulos:.2f}%")
print (f"% votos em branco: {percentBrancos:.2f}%")
