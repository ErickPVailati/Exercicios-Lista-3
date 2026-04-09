class transporte:
    def mover(self):
        print("O transporte está se movendo")
class onibus(transporte):
    def mover(self):
        print("O ônibus está se movendo")

onibus1 = onibus()
onibus1.mover()