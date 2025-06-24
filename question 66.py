palavras = ["Olá", "mundo", "Python"]
separador = "-"

resultado = ""

for i in range(len(palavras)):
    resultado += palavras[i]
    if i < len(palavras) - 1:
        resultado += separador

print (resultado)
