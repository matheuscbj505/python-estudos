#teste1 

carros = ['ferrari', 'fusca', 'civic']
print (carros[-1]) #ultimo elemento da lista 

escola = ['aluno', 'professor', 'livro']
print (escola)

escola.append ('material escolar') #adiciona no final da lista 
print (escola)

escola.insert (1, 'caderno')
print (escola)

escola.extend ('aluno') #separa caracteres da lista 
print (escola)

escola.pop (2) #remove elementos da lista 
print (escola)

escola.remove ('material escolar')
print (escola)

escola.sort () #ordena a lista 
print (escola)  

vetor = [1,4,6,3,2,6,8,9,4,2]
vetor.sort () #ordena vetor 
print (vetor)

vetor.sort(reverse=True) #ordena em ordem contrária 
print (vetor)

print (sorted(vetor))
print(len(vetor)) #informa o tamanho da lista 

#teste2

times = ['atletico-mg', 'cruzeiro', 'santos', 'sao paulo', 'flamengo', 'corinthians']
print (times)
print (times [::-1])

times.append ('internacional')
print (times)

times.insert (3, 'gremio')
print (times)

times.insert (0, 'fluminense')
print (times)

times.sort ()
print (times)

times.sort (reverse=True)
print (times)

print (len(times))

#teste3

times_europeus = ['realmadrid', 'barcelona', 'liverpool', 'chelsea', 'porto']
print (times_europeus)
times_europeus.append ('milan')
print (times_europeus)
times_europeus.insert (5, 'inter_de_milao')
print (times_europeus)
times_europeus.reverse ()
print (times_europeus)
times_europeus.sort()
print (times_europeus)
times_europeus.sort(reverse=True)
print (times_europeus)
times_europeus.pop ()
print (times_europeus)

