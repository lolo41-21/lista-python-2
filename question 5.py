popA = int(input('Digite a população inicial do país A: '))
taxaA = int(input('Digite a taxa de crescimento anual do país A (em %): ')) / 100

popB = int(input('Digite a população inicial do país B: '))
taxaB = int(input('Digite a taxa de crescimento anual do país B (em %): ')) / 100

anos = 0

while popA < popB:
    popA += popA * taxaA
    popB += popB * taxaB
    anos += 1
print (f'A população do país A vai ultrapassar a população do país B em {anos} anos!')