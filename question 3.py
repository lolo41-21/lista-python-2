nome = input("Digite o nome: ")
while len(nome) <= 3:
    print("Nome inválido. Deve ter mais de 3 caracteres.")
    nome = input("Digite o nome: ")

idade = int(input("Digite a idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida. Deve estar entre 0 e 150.")
    idade = int(input("Digite a idade: "))

salario = float(input("Digite o salário: "))
while salario <= 0:
    print("Salário inválido. Deve ser maior que zero.")
    salario = float(input("Digite o salário: "))

sexo = input("Digite o sexo ('f' ou 'm'): ")
while sexo != 'f' and sexo != 'm':
    print("Sexo inválido. Use apenas 'f' ou 'm'.")
    sexo = input("Digite o sexo ('f' ou 'm'): ")

estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ")
while estado_civil not in ['s', 'c', 'v', 'd']:
    print("Estado civil inválido. Use apenas 's', 'c', 'v' ou 'd'.")
    estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ")

print("Informações:")
print("Nome:", nome)
print("Idade:", idade)
print("Salário: R$", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)