class Main:
    pass
print("Testando o projeto")

from Cliente import Cliente
from Conta import Conta
#referência de classe

primeiro_cliente= Cliente(" ")
#declarar um novo objeto =  declarar um nova variavel
#Cliente(strings) = nome da classe instanciada + atributos do metodo construtor


print(primeiro_cliente._nome, " e ", "Nº do CPF:",primeiro_cliente._cpf)
conta= Conta(primeiro_cliente._nome, numero=" ")
print(conta._titular, "Numero da conta:", conta._numero, "Saldo R$:",f"{conta._saldo:.2f}")
