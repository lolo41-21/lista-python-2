def combinar_listas(*listas):
    resultado = []
    for lista in listas:
        resultado.extend(lista)
    return resultado
print(combinar_listas([1, 2], [3, 4], [5]))        
print(combinar_listas(['a'], ['b', 'c'], []))      
print(combinar_listas([10], [20, 30], [40, 50]))   