cidade = ''
while True: 
    print ('para encerrar digite sair')
    cidade = input ('cidade: ')
    if cidade == 'continuar': 
        continue #nao executa o fim do laço e continua o while 
    elif cidade == 'sair':
        break     
    else:
        print (cidade)
    