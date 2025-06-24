texto = 'programação em python'
inicio = 4
fim = 12

inicio = max(0, inicio)
fim = min(len(texto), fim)

substring = texto[inicio : fim]
print (substring)
