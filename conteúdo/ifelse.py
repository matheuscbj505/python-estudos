filmes = ['nemo', 'tarzan', 'carros', 'vingadores']

for filme in filmes: 
    if filme == 'nemo':
        print (filme.upper())
    else:
        print (filme.title()) #deixa a primeira letra em maiúsculo 

nome = input ('digite seu nome: ')
idade = int(input('qual a sua idade: '))
print (nome)
print (idade)

if (idade < 16) or (idade > 64) :
    print ('nao pode votar')
elif idade <= 16 and idade <= 17:
    print ('voto opcional')
else: 
    print ('voto obrigatorio')