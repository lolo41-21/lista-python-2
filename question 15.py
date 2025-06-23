n = int(input("Digite quantos termos da série de Fibonacci você quer ver: "))

a = 1
b = 1

print ("Sequência de Fibonacci:")

for i in range (n):
    print (a)
    proximo = a + b  
    a = b            
    b = proximo