class dispositivo:
    def ligar(self):
        print(f"{self.nome} está ligado.")
        
class celular(dispositivo):
    def tirar_foto(self):
        print(f"{self.nome} tirou uma foto.")
        
        
celular1 = celular()
celular1.nome = "iPhone"
celular1.ligar()
celular1.tirar_foto()
