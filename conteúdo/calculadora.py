print ('caculadora')

ligada = True
while (ligada):
 print ('digite os valores que deseja operar')
 valor1 = float(input('valor1: '))
 valor2 = float(input('valor2: ')) 
 print ('digite a operacao que deseja realizar: ')
 op =  input('operacao')
 if op == '+': 
    print (valor1 + valor2)
 elif op == '-': 
    print (valor1 - valor2)
 elif op == '/': 
    print (valor1 / valor2)
 elif op == '*': 
    print (valor1 * valor2)
 val = int(input ('press 0 to turn off and 1 to keep using: '))
 if val == 0: 
    ligada = False 

