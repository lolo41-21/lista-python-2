totalCds = int(input("Informe a quantidade de CDs: "))
totalInvestido = 0

for i in range(totalCds):
    valor = float(input(f"Informe o valor do CD {i+1}: "))
    totalInvestido += valor

media = totalInvestido / totalCds
print("Valor total investido: R$", totalInvestido)
print("Valor médio gasto por CD: R$", media)
