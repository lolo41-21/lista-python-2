numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
expressao = ""

for i in range(numero, 0, -1):
    fatorial *= i
    expressao += f"{i}."

expressao = expressao.rstrip(".")
print (f"{numero}! = {expressao} = {fatorial}")