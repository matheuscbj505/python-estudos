#É possível declarar uma variável dentro da classe sem a necessidade da passagem por parâmetro
class Carros:

    def __init__(self, km, ano, cor):
        self.km = km
        self.ano = ano
        self.cor = cor
        self.marca = 'Fiat'
        self.tanque = 100

    def descricao (self):
        print ('O carro da marca ' + self.marca)
        print ('Ano: ' + str(self.ano))
        print ('Cor: ' + self.cor)
        print ('Km: ' + str(self.km) + ' km rodados')

    def proprietario (self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def nova_marca (self, marca):
        self.marca = marca 

    def aumenta_km (self, km_rodados):
        self.km += km_rodados # igual à self.km = self.km + km_rodados

    def mostra_tanque (self):
        print ('O tanque de gasolina está ' + str(self.tanque) + ' % cheio ')

class Carros_Eletricos (Carros):
    #Herda todos os atributos de "carros"
    #SuperClasse -> SubClasse
    def __init__(self, km, ano, cor):
        super().__init__(km, ano, cor)
        self.bateria = Bateria ()
        self.piloto_automatico = Self_pilot ('Híbrido', 'Manual')
    
    def mostra_tanque(self):
        print ('carros eletricos nao usam gasolina')


class Self_pilot ():
    
    def __init__(self, modelo, acionamento):
        self.modelo = modelo
        self.acionamento = acionamento

    def set_self_pilot (self, acionamento):     
        self.acionamento = acionamento  
    
    def mostra_self_pilot (self):
        print ('Modelo ' + self.modelo)
        print ('Acionamento ' + self.acionamento)

class Bateria ():

    def __init__(self, bateria = 100):
        self.bateria = bateria

    def altera_bateria (self, novo_valor):
        self.bateria = novo_valor

    
carro1 = Carros_Eletricos (201,202,'red')
carro1.descricao ()
carro1.piloto_automatico()
