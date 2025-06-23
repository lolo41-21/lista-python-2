n = int(input("Digite um número inteiro: "))

totalDivisoes = 0  

for num in range(2, n + 1):  
    divisoesNum = 0      
    ePrimo = True

    for i in range(2, num):
        totalDivisoes += 1
        divisoesNum += 1
        if num % i == 0:
            ePrimo = False
            break  

    if ePrimo:
        print (f"{num} é primo ({divisoesNum} divisões)")

print (f"Total de divisões feitas: {totalDivisoes}")