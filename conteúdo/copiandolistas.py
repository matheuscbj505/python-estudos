                #teste com insetos 
            insetos = ['formiga', 'abelha', 'gafanhoto', 'joaninha']
            insetos2 = insetos [:] #copiando os elementos de insetos para insetos2 
            insetos3 = insetos #se uma lista for alterada a outra também será 
            print (insetos2)
            insetos3.remove ('abelha')
            insetos2.remove ('formiga')
            print (insetos)
            print (insetos2)

            # teste com carros 
            carros = ['corsa', 'picanto', 'civic', 'palio']
            carros2 = carros 
            carros.remove ('corsa')
            print (carros2)
            carros3 = carros [:] 
            carros3.remove ('palio')
            print (carros3)

            #teste com linguagens de programação 
            ling1 = ['c', 'python', 'R', 'basic', 'java']
            ling2 = ling1 [:]
            ling3 = ling2
            ling2.remove ('c') 
            ling3.append ('flutter')
            print (ling2)
            print (ling1)
            print (ling3)
            ling5 = ling2
            ling5.sort
            print (ling5)

