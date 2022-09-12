class Main:
    pass
print("Testando o projeto")

from Cliente import Cliente
from Conta import Conta
from Menu import Menu
#referência de classe

primeiro_cliente= Cliente(" ")
#declarar um novo objeto =  declarar um nova variavel
#Cliente(strings) = nome da classe instanciada + atributos do metodo construtor


conta= Conta(primeiro_cliente._nome, numero=" ")
Menu(" DADOS DO CLIENTE ")
print("CLIENTE: ",conta._titular, "\nNumero da conta:", conta._numero, "\nSaldo R$:",f"{conta._saldo:.2f}")
