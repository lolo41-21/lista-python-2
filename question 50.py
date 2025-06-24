n = int(input("digite o número de termos (N): "))

h = 0
for i in range(1, n + 1):
    h += 1 / i

print (f"\nValor de H com {n} termos: {h:.4f}")
