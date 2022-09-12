from time import sleep

class Conta:
    def __init__(self,titular,numero):
        def leiafloat(n):
            while True:
                try:
                    num = float(input(n))
                except (ValueError, TypeError):
                    print("\033[1;31mERRO! INFORME UM VALOR EM R$\033[m")
                    continue
                except KeyboardInterrupt:
                    print("\n\033[1;31mO USUÁRIO DECIDIU PARAR O PROGRAMA\033[m")
                    return f'\033[7;31;40mNão foi informado nenhum valor\033[m'
                else:  # se tudo der certo, retorne o número informado
                    return num

        # fução leia float, ao qual possui comandos com uso de tratamento de erros
        # em caso do usuário informar um valor errado ou uma string
        print("Digite o valor do seu saldo R$")
        self._saldo= leiafloat(" ")
        self._titular= titular
        print("Digite os 4 ultimos digitos da conta: ")
        self._numero = int(input(" "))


    @property
    def saldo(self):
        return self._saldo


    @saldo.setter
    def saldo(self, saldo):
        if saldo<0:
            print("\033[1;31mO SALDO INFORMADO, NÃO PODE SER NEGATIVO\033[m")
        else:
            self._saldo= saldo
    #funçõão de saque de um determinado valor
    def saque(self, valor):
        if (self.saldo>=valor): #em caso de saldo maior que o valor solicitado
            self.saldo-=valor
            print('.' ,end=" ")
            sleep(0.5)
            print('.' ,end=" ")
            sleep(0.5)
            print('.' ,end=" ")
            sleep(0.5)
            print('\nSAQUE REALIZADO COM SUCESSO')
        else: #se o saldo for inferior ao solicitado
            print('.' ,end=" ")
            sleep(0.5)
            print('.' ,end=" ")
            sleep(0.5)
            print('.' ,end=" ")
            sleep(0.5)
            print("SALDO INSUFICIENTE")

    def deposita(self,valor):
        self.saldo+=valor

    def extrato(self):
        print("O cliente ", self._titular,"\nSaldo atual: ", self._saldo)