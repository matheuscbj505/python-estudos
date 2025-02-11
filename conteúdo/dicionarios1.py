#dicionarios sao representados entre chaves: associação de valores  

alien_0 = {'cor': 'verde', 'pontuacao': 5}
print (alien_0)
alien_0['cor'] = 'azul'
print (alien_0) 
print ('o alien agora tem ' + str(alien_0['pontuacao']) + ' pontos')

sol = {'cor': 'branco', 'galaxia': 'via-lactea', 'composição': 'plasma'}
print (sol)
sol ['principal_composto'] = 'hidrogênio'
print ('o sol, estrela da via lactea, tem uma cor ' + (sol['cor']) + 'e é composto de ' + (sol['principal_composto']))

marca = {'especialidade': 'esporte', 'ano_de_fundação': 2001, 'logo': 'cachorro'}
print (marca)
print ("A marca em questão foi fundada no ano de " + str(marca['ano_de_fundação']) + ' e o seu ramo de atuação é o ' + (marca['especialidade']))






