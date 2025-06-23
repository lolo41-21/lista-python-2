num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

menor = min(num1, num2)
maior = max(num1, num2)

print("Números no intervalo entre", menor, "e", maior, ":")
for i in range(menor + 1, maior):
    print(i)