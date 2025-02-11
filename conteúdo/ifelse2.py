componentens = ['memoria ram', 'processador', 'gpu']
componentes_pedidos =  ['memoria ram', 'processador', 'gpu', 'placa mae']

for componente in componentes_pedidos:
    if componente in componentens:
        print (componente + ' presente na loja')
    else: 
       print (componente + ' nao presente na loja')


presentes = ['relogio', 'celular', 'tenis', 'garrafa', 'calculadora']
presentesdesejados = ['relogio', 'celular', 'anel', 'terno', 'tenis']

for presente in presentes:
    if presente in presentesdesejados:
        print (presente + ' sera aproveitado')
    else:
        print (presente + ' nao sera aproveitado')


numeros_jogados = [4,9,25,27,47,62]
numeros_sorteados = [4,9,25,27,47,62]

cont = 0
for numero in numeros_jogados:
    if numero in numeros_sorteados:
        cont = cont + 1

if cont == 6:
    print ('ganhou na mega')
else:
    print ('perdeu na mega')

