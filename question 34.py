n = int(input("Digite um número inteiro: "))

if n <= 1:
    print(f"{n} não é primo.")
else:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(f"{n} é primo.")
    else:
        print(f"{n} não é primo.")
