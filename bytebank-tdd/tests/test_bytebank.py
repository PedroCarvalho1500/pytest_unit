import pytest
from codigo.bytebank import Funcionario
from pytest import mark

class TestClass: 
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        
        #Given-When-Then Metodologia Ágil para o desenvolvimento de testes.
        #Given
        entrada = '13/03/2000'
        esperado = 22
        funcionario_teste = Funcionario("Teste", entrada, 1111)
        #When
        resultado = funcionario_teste.idade()
        #Then
        assert resultado == esperado
        
        
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        #Given
        entrada = 'Lucas Carvalho'
        esperado = "Carvalho"
        funcionario_teste = Funcionario(entrada, "13/03/2000", 1111)
        #When
        resultado = funcionario_teste.sobrenome()
        #Then
        assert resultado == esperado
        
        
    def test_quando_decrescimo_recebe_1000000_deve_retornar_90000(self):
        #Given
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000
        funcionario_teste = Funcionario(entrada_nome, "13/03/2000", entrada_salario)
        
        #When
        resultado = funcionario_teste.decrescimo()
        
        #Then
        assert resultado == esperado
        
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        #Given
        entrada_salario = 1000
        entrada_nome = "Ana"
        esperado = 100
        funcionario_teste = Funcionario(entrada_nome, "13/03/2000", entrada_salario)
        
        #When
        resultado = funcionario_teste.calcular_bonus()
        
        #Then
        assert resultado == esperado
        
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            
            #Given
            entrada_salario = 10000000
            entrada_nome = "Ana"
            #esperado = "O SALÁRIO É MUITO ALTO PARA RECEBER UM BÔNUS!!!"
            funcionario_teste = Funcionario(entrada_nome, "13/03/2000", entrada_salario)
            
            #When
            resultado = funcionario_teste.calcular_bonus()
            
            #Then
            assert resultado
            
            
            
    #def test_quando_printar_funcionario_deve_retornar_nome_data_salario(self):
            
        #Given
    #    entrada_salario = 1000
        
    #    entrada_nome = "Ana"
        
    #    esperado = f'Funcionario(Ana, 13/03/2000, 1000)'
        
    #    funcionario_teste = Funcionario(entrada_nome, "13/03/2000", entrada_salario)
            
            #When
    #    resultado = funcionario_teste.__str__()
            
            #Then
    #    assert resultado
            
#pytest -k idade (por uma palavra no nome do método)
# pytest --cov=codigo tests/ --cov-report term-missing