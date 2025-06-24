salario = 1000.00
ano = 1995
percentual = 1.5

for atual in range(1996, 2025):  
    aumento = salario * (percentual / 100)
    salario += aumento
    percentual *= 2

print (f"salário atual em {atual}: R$ {salario:.2f}")

salario = float(input("digite o salário inicial: R$ "))
ano = 1995
percentual = 1.5

for atual in range(1996, 2025): 
    aumento = salario * (percentual / 100)
    salario += aumento
    percentual *= 2

print (f"salário atual em {atual}: R$ {salario:.2f}")
