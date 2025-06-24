temps = []
while True:
    temp = float(input("Informe a temperatura (0 para terminar): "))
    if temp == 0:
        break
    temps.append(temp)

if temps:
    print ("menor temperatura:", min(temps))
    print ("maior temperatura:", max(temps))
    print ("media das temperaturas: ".format(sum(temps)/len(temps)))
else:
    print ("nenhuma temperatura foi informada.")
