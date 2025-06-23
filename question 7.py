maior = int(input("Digite um número: "))
for i in range(4):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num

print("O maior número é:", maior)