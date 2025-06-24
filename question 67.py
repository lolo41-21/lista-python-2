texto = "desenvolvimento Web"
padrao1 = "desen"
padrao2 = "web"
padrao3 = "mobile"

if texto[len(padrao1)] == padrao1:
    print ("É prefixo")
else:
    print ("Não é prefixo")

if texto[len(padrao2):] == padrao2:
    print ("É sufixo")
else:
    print ("Não é sufixo")

if texto[len(padrao3)] == padrao3:
    print ("É prefixo")
else:
    print ("Não é prefixo")

if texto[len(padrao3):] == padrao3:
    print ("É sufixo")
else:
    print ("Não é sufixo")
