n = int(input("Quantas pessoas há na turma? "))

if n > 0:
    soma = 0

    for i in range(n):
        idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
        soma += idade
        
    media = soma / n
    print (f"Média de idade: {media}")

    if media <= 25:
        print ("A turma é jovem.")
    elif media <= 60:
        print ("A turma é adulta.")
    else:
        print ("A turma é idosa.")
else:
    print ("Número de pessoas deve ser maior que zero.")
