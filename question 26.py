v1 = 0
v2 = 0
v3 = 0
n = int(input("total de eleitores: "))

for i in range(n):
    voto = int(input("vote (1, 2 ou 3): "))
    if voto == 1: v1 += 1
    elif voto == 2: v2 += 1
    elif voto == 3: v3 += 1

print (f"candidato 1: {v1} votos")
print (f"candidato 2: {v2} votos")
print (f"candidato 3: {v3} votos")