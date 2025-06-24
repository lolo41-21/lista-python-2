cont025 = cont2650 = cont5175 = cont76100 = 0

while True:
    num = int(input("Número positivo (negativo para sair): "))
    if num < 0:
        break
    if num <= 25:
        cont025 += 1
    elif num <= 50:
        cont2650 += 1
    elif num <= 75:
        cont5175 += 1
    elif num <= 100:
        cont76100 += 1

print (f"[0-25]: {cont025}")
print (f"[26-50]: {cont2650}")
print (f"[51-75]: {cont5175}")
print (f"[76-100]: {cont76100}")
