n = int(input("digite um número inteiro: "))

primos = []

for num in range(2, n + 1):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        primos.append(num)

print ("numeros primos entre 1 e", n, ":", primos)
