def calcular_fatorial(numero):
    if numero < 0:
        return "erro: número negativo não possui fatorial."
    elif numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

print(calcular_fatorial(5))           
print(calcular_fatorial(0))           
print(calcular_fatorial(-3))          

print(calcular_fatorial(5)) 
