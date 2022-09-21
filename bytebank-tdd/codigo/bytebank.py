#python3 -m venv venv
# source venv/bin/activate
from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')

        
        ano_nascimento = data_nascimento_quebrada[-1]
        
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)
    
    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(" ")
        return nome_quebrado[-1]
    
    def eh_socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self.salario >= 100000 and self.sobrenome() in sobrenomes)

    
    def decrescimo(self):
        if(self.eh_socio()):
            salario_com_decrescimo = float(self.salario) - (float(self.salario) * 0.1)
            return float(salario_com_decrescimo)




    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("O SALÁRIO É MUITO ALTO PARA RECEBER UM BÔNUS!!!")
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'