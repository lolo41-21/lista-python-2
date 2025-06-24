texto = input("Digite uma string: ")

vogais = "aeiou"
totalVogais = 0
totalConsoantes = 0

for caractere in texto:
    if caractere.isalpha(): 
        if caractere in vogais:
            totalVogais += 1
        else:
            totalConsoantes += 1

print(f"\nNumero de vogais: {totalVogais}")
print(f"Numero de consoantes: {totalConsoantes}")
