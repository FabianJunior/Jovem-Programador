#classe do professor

class Clientes():
    def __init__(self):
        self.id=None
        self.nome=None
        self.email=None
        self.cpf=None
        self.usuario_id=None
    def banco_para_modelo(self,cliente_banco):
        self.id=cliente_banco(0)
        self.nome=cliente_banco(1)
        self.email=cliente_banco(2)
        self.cpf=cliente_banco(3)
        self.usuario_id=cliente_banco(4)
class Usuarios():
    def __init__(self):
        self.usuario=None
        self.senha=None
    def banco_para_modelo(self,usuario_banco):
        self.usuario=usuario_banco
        self.senha=usuario_banco

class Carro():
    def __init__(self):
        self.marca=None
        self.modelo=None
        self.ano=None
    def banco_para_modelo(self,carro_banco):
        self.marca=carro_banco(0)
        self.modelo=carro_banco(1)
        self.ano=carro_banco(2)
    def inserir_valores(self,marca,modelo,ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
class adms():
    def __init__(self):
        self.usuario=None
        self.senha=None
        self.cpf=None
        self.email=None
    def banco_para_modelo(self,adms_banco):
        self.usuario=adms_banco(0)
        self.senha=adms_banco(1)
        self.cpf=adms_banco(2)
        self.email=adms_banco(3)