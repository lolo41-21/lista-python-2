num = int(input("montar a tabuada de: "))
inicio = int(input("começar por: "))
fim = int(input("terminar em: "))

print (f"tabuada de {num} começando em {inicio} e terminando em {fim}:")

for i in range(inicio, fim + 1):
    print(f"{num} X {i} = {num * i}")
