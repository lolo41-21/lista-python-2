n = int(input("Quantos números terão no conjunto? "))
numeros = []

for i in range(n):
    valor = float(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print (f"Menor valor: {menor}")
print (f"Maior valor: {maior}")
print (f"Soma dos valores: {soma}")