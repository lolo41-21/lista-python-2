def sao_anagramas(palavra1, palavra2):
    limpa1 = palavra1.replace(" ", "").lower()
    limpa2 = palavra2.replace(" ", "").lower()

    return sorted(limpa1) == sorted(limpa2)

print (sao_anagramas("Roma", "Amor"))            
print (sao_anagramas("Conversar", "Conversão"))  
print (sao_anagramas("Aroma", "Amora"))          
print (sao_anagramas("Escuta", "Acetus"))        
print (sao_anagramas("Olha", "Olá"))             