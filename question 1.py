while True:
        nota = float(input('Digite uma nota de 0 a 10: '))
        if 0 <= nota <= 10:
            print (f'Nota: {nota}')
            break
        else:
            print ('valor inválido!')