popA = 80000
taxaCrescimentoA = 3.0
popB = 200000
taxaCrescimentoB = 1.5

anos = 0

while popA < popB:
    popA += popA * (taxaCrescimentoA / 100)
    popB += popB * (taxaCrescimentoB / 100)
    anos += 1

print ("No mínimo", anos, "anos para que a população do país A ultrapasse ou iguale a do país B.")