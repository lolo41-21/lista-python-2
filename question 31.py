while True:
    print ("Lojas Tabajara")
    total = 0
    produto = 1

    while True:
        preco = float(input(f"Produto {produto}: R$ "))
        if preco == 0:
            break
        total += preco
        produto += 1

    print (f"Total: R$ {total}")
    
    dinheiro = float(input("Dinheiro: R$ "))
    troco = dinheiro - total

    print (f"Troco: R$ {troco}")

    continuar = input("Nova compra? (s/n): ").lower()
    if continuar != 's':
        break
