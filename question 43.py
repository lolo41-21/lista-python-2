cardapio = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20, 104: 1.30, 105: 1.00}

totalGeral = 0

while True:
    codigo = int(input("Digite o código do item (0 para encerrar): "))
    if codigo == 0:
        break

    quantidade = int(input("quantidade: "))
    preco = cardapio[codigo]
    totalItem = preco * quantidade
    totalGeral += totalItem

    print(f"Valor a pagar pelo item {codigo}: R$ {totalItem:.2f}")

print(f"\nTotal geral do pedido: R$ {totalGeral:.2f}")
