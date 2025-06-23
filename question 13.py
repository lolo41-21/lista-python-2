base = int(input('Digite o 1° número: '))
expo = int(input('Digite seu expoente: '))

resultado = 1
for i in range(expo):
    resultado *= base
print (f'{base} elevado a {expo} é igual a: {resultado}')