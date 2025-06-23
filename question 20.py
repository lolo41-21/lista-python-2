n = int(input("Digite um número de 0 a 16: "))
numeros = []

if n < 16 and n > 0:

    for i in range(n):
        valor = float(input(f"Digite o {i+1}º número: "))
        numeros.append(valor)

    menor = min(numeros)
    maior = max(numeros)
    soma = sum(numeros)

    print (f"Menor valor: {menor}")
    print (f"Maior valor: {maior}")
    print (f"Soma dos valores: {soma}")
else:
    print ('Digite um número entre 0 e 16')