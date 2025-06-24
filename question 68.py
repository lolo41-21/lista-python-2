def calculadora (num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 == 0:
            return "Erro: divisão por zero"
        return num1 / num2
    
print(calculadora(10, 5, 'soma'))          
print(calculadora(10, 5, 'subtracao'))      
print(calculadora(10, 5, 'multiplicacao'))  
print(calculadora(10, 5, 'divisao'))        
print(calculadora(10, 0, 'divisao'))        
print(calculadora(10, 5, 'potencia')) 