def converter_temperatura(valor, unidadeOrigem, unidadeDestino):
    unidadeOrigem = unidadeOrigem.upper()
    unidadeDestino = unidadeDestino.upper()

    unidadesValidas = ['C', 'F', 'K']
    if unidadeOrigem not in unidadesValidas or unidadeDestino not in unidadesValidas:
        return "Erro: unidade inválida. Use 'C', 'F' ou 'K'."

    if unidadeOrigem == unidadeDestino:
        return valor

    if unidadeOrigem == 'F':
        valorCelsius = (valor - 32) / 1.8
    elif unidadeOrigem == 'K':
        valorCelsius = valor - 273.15
    else:
        valorCelsius = valor  

    if unidadeDestino == 'F':
        convertido = valorCelsius * 1.8 + 32
    elif unidadeDestino == 'K':
        convertido = valorCelsius + 273.15
    else:
        convertido = valorCelsius  

    return convertido
print (converter_temperatura(0, 'C', 'F'))   
print (converter_temperatura(100, 'C', 'K'))
print (converter_temperatura(32, 'F', 'C'))  
print (converter_temperatura(300, 'K', 'C'))
print (converter_temperatura(212, 'F', 'K')) 
print (converter_temperatura(273.15, 'K', 'F')) 
print (converter_temperatura(100, 'X', 'C')) 
