texto = input("digite uma frase ou palavra: ")

texto = texto.replace(" ", "")

print (texto == texto[::-1])
