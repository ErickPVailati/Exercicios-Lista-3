class forma():
    def area():
        area = 0
        return area
        
class quadrado(forma):
    def __init__(self, lado):
        self.lado = lado
        self.area = self.lado * self.lado
        
quadrado.lado = int(input("Digite o valor do lado do quadrado: "))
quadrado = quadrado(quadrado.lado)
print("Área do quadrado: ", quadrado.area)
        



    

