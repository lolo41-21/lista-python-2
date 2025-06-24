preco = float(input("Preço do pão: R$ "))

print ("Panificadora Pão de Ontem - Preços")
for i in range(1, 51):
    total = i * preco
    print (f"{i} - R$ {total}")
