personagem = {'xp': 12, 'stamina':23, 'power':21, 'inteligence':33, 'defense':43, 'magic':40}
print (personagem)
del personagem ['power']
print (personagem)

for atr, val in personagem.items():
    print (atr, val)

aviao = {'companhia': 'gol', 'fabricante': 'boing'}
print (aviao['companhia'])
aviao['companhia'] = 'tam'
del aviao ['fabricante']
print (aviao)

jogador = {'força': 78, 'passe': 89, 'finalização': 88, 'drible': 77}
print (jogador)
jogador ['arranque'] = 89
print (jogador)
del jogador ['força']
print (jogador)

livro = {'paginas': 104, 'gênero': 'ficção', 'autor': 'zedascouve', 'ano_lançamento': 2008}
print (livro)
del livro['ano_lançamento']
print (livro)
livro ['copias_vendidas'] = 50000
print (livro)

país = {'n_habitantes': 4000, 'idioma': 'latim', 'idh': 5, 'pib': 40}
print (país)
del país ['idioma']
print (país)
país ['gini'] = 7








