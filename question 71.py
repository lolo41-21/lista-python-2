def validar_email(email):
    if email.count('@') != 1:
        return False

    parteAntes, parteDepois = email.split('@')

    if len(parteAntes) < 1:
        return False

    if '.' not in parteDepois:
        return False

    dominio, *extensao = parteDepois.split('.', 1)

    if len(dominio) < 1:
        return False

    if len(extensao) == 0 or len(extensao[0]) < 2:
        return False

    return True

print (validar_email("usuario@dominio.com"))      
print (validar_email("a@b.co"))                   
print (validar_email("usuario@dominio."))         
print (validar_email("@dominio.com"))             
print (validar_email("usuario@.com"))             
print (validar_email("usuario@dominio.c"))        
print (validar_email("usuario@@dominio.com"))