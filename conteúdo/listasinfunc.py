'''
compras = ["sabonete", "shampoo", "cereal", "arroz"]
for compra in compras:
    print (compra)


def lista_de_compras (lista):
    lista.pop()

lista_de_compras (compras) #altera o valor original da lista 
lista_de_compras (compras [:]) #traz como argumento uma copia da lista 
'''

def pop (lista):
     lista.pop ()
     lista.pop ()
     print (lista)

cores = ['azul', 'verde', 'amarelo', 'vermelho', 'roxo']

pop (cores) #cria uma copia da lista
print (cores)



