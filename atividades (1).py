import sys
from PyQt5 import uic, QtWidgets
import funçoes
import banco
from classes import Clientes,Usuarios,Carro,adms

def buscar_pessoa():
    cpf_input=tela_clientes.inputcpf.text()
    cpf_input=funçoes.limpar_campo_cpf(tela_clientes.inputcpf.text())
    pessoa=banco.buscar_pessoa_por_cpf(cpf_input)
    if pessoa is None:
        tela_clientes.close()
        tela_mensagem.show()
    else:
        carros=banco.buscar_carro_por_pessoa_id(pessoa[0])
        for c in carros:
            tela_clientes.listacarros.addItem(f'marca{c[0]} modelo{c[1]} ano{c[2]}')     
def fechar_tela_mensagem_criar_pessoa():
    tela_mensagem.close()
    tela_clientes.show()
def abrir_tela_conta_nova():
    tela_cadastro_pessoa.show()
    tela_mensagem.close()
def fechar_tela_cadastro_pessoa():
    tela_cadastro_pessoa.close()
    tela_clientes.show()
def criar_pessoa():
    nome=tela_cadastro_pessoa.inputnome.text()
    cpf_input=funçoes.limpar_campo_cpf(tela_cadastro_pessoa.inputcpf.text())
    email=tela_cadastro_pessoa.inputemail.text()
    novo_id=tela_cadastro_pessoa.inputid.text()
    pessoa=banco.buscar_pessoa_por_cpf(cpf_input)
    if pessoa is not None:
        tela_mensagem_erro.label.setText('CPF JA CADASTRADO')
        abrir_tela_avisos()
    elif cpf_input=='' or nome=='' or email=='' or novo_id=='':
        tela_mensagem_erro.label.setText('TODOS OS CAMPOS DEVEM SER PREENCHIDOS')
        abrir_tela_avisos()
    else:
        banco.inserir_pessoa(nome,cpf_input,email,novo_id)
        fechar_tela_cadastro_pessoa
        abrir_tela_clientes
def abrir_tela_avisos():
    tela_mensagem_erro.show()      
def fechar_tela_avisos():
    tela_mensagem_erro.close()
def abrir_tela_clientes():
    tela_login.close()
    tela_clientes.show()
def acesso_cliente():
    usuario=tela_login.input_usuario.text()
    senha=tela_login.input_passoword.text()
    pessoa=banco.buscar_pessoa_por_senha(senha)
    if pessoa is None:
        tela_login.situacao_entrada.setText('USUARIOS E SENHAS NÃO EXISTEM')
    elif usuario=='' or senha=='':
        tela_login.situacao_entrada.setText('COLOQUE SEU USUARIO E SENHA CORRETAS')
    else:
        tela_login.close()
        tela_clientes.show()
def inicio_da_tela():
    tela_login.show()
def criar_login():
    usuario_novo=tela_login.input_usuario.text()
    senha_novo=tela_login.input_passoword.text()
    pessoa=banco.buscar_pessoa_por_senha(senha_novo)
    if usuario_novo=='' or senha_novo=='':
        tela_login.situacao_entrada.setText('Digite os Campos') 
    elif pessoa is not None:
        tela_login.situacao_entrada.setText('Ja existe')
    else:
        banco.inserir_pessoa_no_site(usuario_novo,senha_novo)
        tela_login.input_passoword.setText('')
        tela_login.situacao_entrada.setText('--CONTA CRIADA COM SUCESSO--')
def aperto_criar():
    tela_login.close()
    tela_novo_usuario.show()
def criar_adms():
    tela_criar_adm.show()
    tela_novo_usuario.close()
def criando_adm():
    usuario=tela_criar_adm.login_adm.text()
    senha=tela_criar_adm.senha_adm.text()
    rep_senha=tela_criar_adm.rep_senha_adm.text()
    cpf_adm=tela_criar_adm.cpf_adm.text()
    cpf_adm=funçoes.limpar_campo_cpf(tela_clientes.inputcpf.text())
    email_adm=tela_criar_adm.email_adm.text()
    codigos=tela_criar_adm.codigo_adm.text()
    tela_criar_adm.alerta.setText('')
    pessoa=banco.buscar_pessoa_por_cpf(cpf_adm)
    if pessoa is not None:
        tela_criar_adm.alerta.setText('JÁ EXISTE')
    elif usuario== '' or senha=='' or rep_senha=='' or cpf_adm=='' or email_adm=='' or codigos=='':
        tela_criar_adm.alerta.setText('PREENCHAR TODOS OS DADOS')
    elif usuario !='Fabian':
        tela_criar_adm.alerta.setText('NÃO EXISTE ESSE ADM')
    elif senha!=rep_senha:
        tela_criar_adm.alerta.setText('SENHA INVALIDAS')
    elif codigos=='1':
        banco.inserir_adms_no_site(usuario,senha,cpf_adm,email_adm)
        banco.inserir_pessoa_no_site(usuario,senha)
        tela_conf.show()
        tela_criar_adm.close()
def abrir_inicio_login():
    tela_login.show()
def abrir_tela_carros():
    tela_carros.show()
    tela_clientes.close()
def abrir_tela_mensagem():
    tela_mensagem.show()
def criar_carro():
    marca=tela_carros.inputmarca.text()
    Modelo=tela_carros.inputmodelo.text()
    ano= tela_carros.inputano.text()
    carros=banco.inserir_carro(marca,Modelo,ano)
    renderizar()
    tela_carros.close()
    tela_carros.show()
def renderizar():
    carros=banco.criar_tabela_carros()
    row=0
    while(tela_carros.listagem_carro.rowCount()>0):tela_carros.listagem_carro.removeRow(0)
    for i in carros:
        tela_carros.listagem_carro.insertRow(tela_carros.listagem_carro.rowCount())
        tela_carros.listagem_carro.setItem(row,0,QtWidgets.QTableWidgetItem(str(i[0])))
        tela_carros.listagem_carro.setItem(row,1,QtWidgets.QTableWidgetItem(str(i[1])))
        tela_carros.listagem_carro.setItem(row,2,QtWidgets.QTableWidgetItem(str(i[2])))
def fechar_tela_carro():
    tela_carros.close()
    tela_clientes.show()
def deletar_carro():
    carro_del=tela_carros.inputmodelo.text()
    banco.deletar_carro_por_modelo(carro_del)
    renderizar()
    tela_carros.close()
    tela_carros.show()
def modificar_carro():
    marca=tela_carros.inputmarca.text()
    Modelo=tela_carros.inputmodelo.text()
    ano= tela_carros.inputano.text()
    carro=banco.alterar_carro(marca,Modelo,ano)
    renderizar()
    tela_carros.close()
    tela_carros.show()


#CODIGOS :LOAD----FUNÇÕES TELAS----
if __name__=="__main__":
    qt=QtWidgets.QApplication(sys.argv)
    cliente1=Clientes()
    usuario1=Usuarios()
    carro1=Carro()
    adms1=adms()
     #telas LOADS
    tela_login=uic.loadUi('entrada_site_login_inicio.ui')
    tela_novo_usuario=uic.loadUi('conta_nova_login.ui')
    tela_criar_adm=uic.loadUi('adm.ui')
    tela_conf=uic.loadUi('acesso_adm.ui')
    tela_clientes=uic.loadUi('cpf.ui')
    tela_mensagem=uic.loadUi('criar.ui')
    tela_cadastro_pessoa=uic.loadUi('conta_nova.ui')
    tela_mensagem_erro=uic.loadUi('avisos.ui')
    tela_carros=uic.loadUi('carros.ui')
    
     #telas INICIO 
    tela_login.entrar_login.clicked.connect(acesso_cliente)
    tela_login.adm.clicked.connect(criar_adms)
    tela_login.criador.clicked.connect(criar_login)
    
     #telas CONF
    tela_criar_adm.adm_novo.clicked.connect(criando_adm)
     #telas CLIENTE CPF
    tela_clientes.pushButton.clicked.connect(buscar_pessoa)
    tela_clientes.add_carro.clicked.connect(abrir_tela_carros)
    tela_clientes.volta_inicio.clicked.connect(abrir_inicio_login)
    
     #telas carros
    tela_mensagem.opcaonao.clicked.connect(fechar_tela_mensagem_criar_pessoa)
    tela_mensagem.opcaosim.clicked.connect(abrir_tela_conta_nova)
    tela_mensagem.adm.clicked.connect(criar_adms)
    
     #telas carros
    tela_cadastro_pessoa.criar.clicked.connect(criar_pessoa)
    tela_cadastro_pessoa.cancelar.clicked.connect(fechar_tela_cadastro_pessoa)
     
     #telas carros
    tela_mensagem_erro.ok.clicked.connect(inicio_da_tela)
    
     #telas carros
    tela_conf.inicio_adm.clicked.connect(abrir_inicio_login)
    tela_conf.cpf_adm.clicked.connect(abrir_tela_clientes)
    tela_conf.avisos_adm.clicked.connect(abrir_tela_avisos)
    tela_conf.carros_adm.clicked.connect(abrir_tela_carros)
    tela_conf.conta_nova.clicked.connect(abrir_tela_conta_nova)
    tela_conf.criacao_adm.clicked.connect(abrir_tela_mensagem)
    
    #telas carros
    tela_carros.criar_carro.clicked.connect(criar_carro)
    tela_carros.volta_clientes.clicked.connect(fechar_tela_carro)
    tela_carros.deletar_carro.clicked.connect(deletar_carro)
    
    tela_login.show()
    qt.exec_()