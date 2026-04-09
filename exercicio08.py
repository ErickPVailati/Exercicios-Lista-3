class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class desconto(produto):
    def __init__(self, nome, preco, percentual):
        super().__init__(nome, preco)
        self.percentual = percentual

    def calcular_desconto(self):
        desconto_valor = self.preco * (self.percentual / 100)
        preco_com_desconto = self.preco - desconto_valor
        print(f"O preço do {self.nome} com {self.percentual}% de desconto é R${preco_com_desconto:.2f}.")
        
produto1 = desconto("Notebook", 2000, 15)
produto1.calcular_desconto()
