# Abre o arquivo texto.txt no modo leitura ('r')
arquivo = open('letras.txt', 'r')

# Itera sobre cada linha no arquivo
for linha in arquivo:
    # Imprime a linha atual
    print(linha)

# Fecha o arquivo após a leitura
arquivo.close()


