class animal:
    def comer(self):
        print("O animal está comendo.")
class gato(animal):
    def comer(self):
        print("O gato está comendo ração.")
        
gato1 = gato()
gato1.comer()