def desenhar_triangulo(altura, tipo):
    if altura <= 0:
        print ("Erro: altura deve ser um inteiro positivo.")
        return

    for i in range(1, altura + 1):
        if tipo == 'esquerda':
            print ('*' * i)
        elif tipo == 'direita':
            print (' ' * (altura - i) + '*' * i)
        elif tipo == 'centralizado':
            espacos = altura - i
            asteriscos = 2 * i - 1
            print (' ' * espacos + '*' * asteriscos)
        else:
            print ("Erro: tipo inválido. Use 'esquerda', 'direita' ou 'centralizado'.")
            break

desenhar_triangulo(4, 'esquerda')
print()
desenhar_triangulo(4, 'direita')
print()
desenhar_triangulo(4, 'centralizado')

