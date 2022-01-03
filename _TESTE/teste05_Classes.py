# Comando abaixo limpa o terminal antes de executar o próximo código
print("\x1bc")

# exercicio tirado do video abaixo.
# https://www.youtube.com/watch?v=j6B8shHXzks

class Computador:
    def __init__(self, marca, memoriaRam, placaVideo):
        self.marca = marca
        self.memoriaRam = memoriaRam
        self.placaVideo = placaVideo

    def ligar(self):
        print('estou ligando')
    
    def desligar(self):
        print('estou desligando')
    
    def exibirInformacoesDesteComputador(self):
        print(self.marca, self.memoriaRam, self.placaVideo)


# pc1 = Computador('gigabyte', '8gb', 'nvidia')
# pc1.ligar()
# pc1.desligar()
# pc1.exibirInformacoesDesteComputador()

class Carro:
    def __init__(self, modelo, cor, velMax):
        self.modelo = modelo
        self.cor = cor
        self.velMax = velMax
    
    def ligar(self):
        print('carro ligando')
    
    def desligar(self):
        print('carro desligando')

    def defeito(self, estado):
        if estado == False:
            print("funcionando")
        else:
            print("defeito")


    def informacoesCarro(self):
        print(self.modelo, self.cor, self.velMax)

carro1 = Carro('chevette', 'rosa', '140km/h')
carro1.informacoesCarro()
carro1.defeito(False)
carro1.ligar()
carro1.desligar()




