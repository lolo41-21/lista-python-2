n = int(input("Fatorial de: "))

fatorial = 1
fatores = "."

for i in range(n, 0, -1):
    fatorial *= i
    fatores += str(i)
    if i > 1:
        fatores += " . "

print(f"{n}! = {fatores} = {fatorial}")