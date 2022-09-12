class Main:
    pass
print("Testando o projeto")

from Cliente import Cliente
from Conta import Conta
#referência de classe

primeiro_cliente= Cliente("João","31987651234")
#declarar um novo objeto =  declarar um nova variavel
#Cliente(strings) = nome da classe instanciada + atributos do metodo construtor


print(primeiro_cliente.nome, " e ", "Nº de telefone:",primeiro_cliente.telefone)
conta= Conta(primeiro_cliente.nome, 450, 0)
print(conta.titular, "Numero da conta:", conta.numero, "Saldo R$:",conta.saldo)