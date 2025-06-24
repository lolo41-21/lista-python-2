n = int(input("digite o número de termos da série: "))

soma = 0
denominador = 1

print ("\nSérie:")
for i in range(1, n + 1):
    termo = i / denominador
    print (f"{i}/{denominador}")
    soma += termo
    denominador += 2

print (f"\nSoma da série: {soma:.4f}")
