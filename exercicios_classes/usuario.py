#convenção -> nome da classe com primeira letra em maiusculo 

class Usuario:

    def __init__(self, primeiro_nome, ultimo_nome, cpf, cep, id, email):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.cpf = cpf
        self.cep = cep
        self.id = id
        self.email = email 

    def descricao (self):
        print (f'NOME: {self.primeiro_nome.title()} {self.ultimo_nome.title ()}')
        print ('CPF: ' + str(self.cpf))
        print ('CEP: ' + str(self.cep))
        print ('id: ' + str(self.id))
        print ('email: ' + self.email)

    def saudacao (self):
        print ('Olá ' + self.primeiro_nome + ' ' + self.ultimo_nome + ', bem vindo à ótica Seu Olho, Sua vista')

    

usuario1 = Usuario ('João', 'Pedro', 15466577921, 31120000, 105, 'joaopedrosilva@gamil.com')
usuario1.descricao ()
usuario1.saudacao ()
