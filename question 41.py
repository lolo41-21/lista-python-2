valorDivida = float(input("Digite o valor da dívida: R$ "))

print("\nValor da Dívida  Valor dos Juros  Parcelas  Valor da Parcela")

for parcelas, juros in [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]:
    valorJuros = valorDivida * (juros / 100)
    valorTotal = valorDivida + valorJuros
    valorParcela = valorTotal / parcelas

    print(f"R$ {valorTotal:10.2f}  R$ {valorJuros:12.2f}  {parcelas:8}  R$ {valorParcela:14.2f}")
