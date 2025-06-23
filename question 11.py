num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

menor = min(num1, num2)
maior = max(num1, num2)

if maior - menor <= 1:
    print("Não há números inteiros nesse intervalo.")
else:
    print(f"Números no intervalo entre", menor, "e", maior, ":")

    soma = 0

    for i in range(menor + 1, maior):
        print(i)
        soma += i
    print("Soma dos números no intervalo:", soma)