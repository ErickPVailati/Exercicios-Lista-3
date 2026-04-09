class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
        
class estudante(pessoa):
    def __init__(self, nota):
        self.nota = nota

    def apresentar(self):
        super().apresentar()
        print(f"Minha nota é {self.nota}.")

estudante1 = estudante(8.5)
estudante1.nome = "João"
estudante1.idade = 20
estudante1.apresentar()