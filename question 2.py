while True:
    usuario = input('Digite o nome de usuario: ')
    senha = input('Digite a senha: ')

    if usuario == senha:
        print ('a senha deve ser diferente do nome de usuario!')
    
    else:
        print ('cadastro feito com sucesso!')
    break