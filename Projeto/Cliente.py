class Cliente:
    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone
        #parametros n e fone são criados para inicialização dos atributos

    #comando pass= nenhuma estrutura foi definida ainda

    #Método GET - acessar atributos que estão privados

    def get_nome(self):
        return self._nome

    #Método SET

    def set_nome(self, nome):
        self._nome= nome