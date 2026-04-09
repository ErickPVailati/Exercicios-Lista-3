class Veiculo:
    def __init__(self, velocidade):
        self.velocidade = velocidade
        
    def mostrar_velocidade(self):
        print(f"Velocidade: {self.velocidade} km/h")
     
class Carro(Veiculo):
    def __init__(self, velocidade):
        super().__init__(velocidade)

    def abrir_porta(self):
        print("Porta do carro aberta.")
        
chevete = Carro(120)

chevete.mostrar_velocidade()
chevete.abrir_porta()
