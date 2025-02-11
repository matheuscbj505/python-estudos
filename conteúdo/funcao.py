#def = para definir uma função 

def soma (val1, val2): #parametors
    print (val1 + val2)

def sub (val1, val2):
    print (val1 - val2)

def mult (a, b):
    print (a*b)

def calculadora ():
    val1 = int(input('val1: '))
    val2 = int(input('val2: '))
    soma (val1, val2)
    sub  (val1, val2)
calculadora ()