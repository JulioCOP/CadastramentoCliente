class Cliente:
    def __init__(self, cpf):
        print("Informe o nome do cliente: ")
        self._nome = str(input(" "))
        print("Digite os 11 NUMEROS do CPF")
        def leiaint(n):
            while True:
                try:
                    num = int(input(n))
                except (ValueError, TypeError):
                    print("\033[1;31mERRO! INFORME UM VALOR INTEIRO\033[m")
                    continue
                except KeyboardInterrupt:
                    print("\n\033[1;31mO USUÁRIO DECIDIU PARAR O PROGRAMA\033[m")
                    return f'\033[7;31;40mNão foi informado nenhum valor\033[m'
                else:  # se tudo der certo, retorne o número informado
                    return num
        self._cpf = leiaint(" ")

        #parametros n e fone são criados para inicialização dos atributos

    #comando pass= nenhuma estrutura foi definida ainda

    #Método GET - acessar atributos que estão privados

    def get_nome(self):
        return self._nome

    #Método SET

    def set_nome(self, nome):
        self._nome= nome