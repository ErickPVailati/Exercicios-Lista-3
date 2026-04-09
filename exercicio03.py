class funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def calcular_salario(self):
        return self.salario
    
    
class gerente(funcionario):
    def calcular_bonus(self):
            return self.salario * 0.1
        
        
    def calcular_bonus(self):
        return self.salario * 0.2
    
    
    
Maicon = gerente("Maicon", 5000)
print("Salário do gerente: ", Maicon.calcular_salario())
print("Bônus do gerente: ", Maicon.calcular_bonus())

Juliane = funcionario("Juliane", 3000)
print("Salário do funcionário: ", Juliane.calcular_salario())

