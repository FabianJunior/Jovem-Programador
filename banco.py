
import sqlite3

def conectar():
    banco=sqlite3.connect('banco.db')
    return banco
def criar_tabela_usuarios():
    banco=conectar()
    cursor=banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(usuario TEXT,senha TEXT);')
    banco.commit()
    banco.close()
def adms():
    banco=conectar()
    cursor=banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS adms(usuario TEXT,senha TEXT,cpf TEXT,email TEXT);')
    banco.commit()
    banco.close()
def inserir_pessoa_no_site(usuario,senha):
    banco=sqlite3.connect('banco.db')
    cursor=banco.cursor()
    adms()
    criar_tabela_usuarios()
    cursor.execute(f"INSERT INTO usuarios VALUES('{usuario}','{senha}');")
    banco.commit()
    banco.close()
def inserir_adms_no_site(usuario,senha,cpf,email):
    banco=sqlite3.connect('banco.db')
    cursor=banco.cursor()
    adms()
    criar_tabela_usuarios()
    cursor.execute(f"INSERT INTO adms VALUES('{usuario}','{senha}','{cpf}','{email}');")
    banco.commit()
    banco.close()
def buscar_pessoa_por_senha(senha):
    banco=conectar()
    cursor=banco.cursor()
    adms()
    criar_tabela_usuarios()
    cursor.execute(f"SELECT * FROM usuarios WHERE senha='{senha}' ")
    return cursor.fetchone()

def criar_tabela_pessoas():
    banco=conectar()
    cursor=banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS pessoas(nome TEXT,email TEXT,cpf TEXT,pessoa_id INTERGER NOT NULL,FOREIGN KEY(pessoa_id) REFERENCES pessoa(id));')
    banco.commit()
    banco.close()


def criar_tabela_carros():
    banco=conectar()
    cursor=banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS carros(marca TEXT,modelo TEXT,ano TEXT);')
    banco.commit()
    banco.close()


def inserir_pessoa(nome,email,cpf,pessoa_id):
    banco=sqlite3.connect('banco.db')
    cursor=banco.cursor()
    criar_tabela_pessoas()
    cursor.execute(f"INSERT INTO pessoas VALUES('{nome}','{email}','{cpf}','{pessoa_id}');")
    banco.commit()
    banco.close()


def inserir_carro(marca,modelo,ano):
    banco=sqlite3.connect('banco.db')
    cursor=banco.cursor()
    criar_tabela_carros()
    cursor.execute(f"INSERT INTO carros VALUES('{marca}','{modelo}','{ano}');")
    banco.commit()
    banco.close()


def buscar_pessoa_por_cpf(cpf):
    banco=conectar()
    cursor=banco.cursor()
    criar_tabela_pessoas()
    cursor.execute(f"SELECT rowid, * FROM pessoas WHERE cpf='{cpf}' ")
    return cursor.fetchone()


def buscar_carro_por_ano(ano):
    banco=conectar()
    cursor=banco.cursor()
    criar_tabela_carros()
    cursor.execute(f"SELECT * FROM carros WHERE ano={ano};")
    return cursor.fetchall()


def buscar_carro_por_marca(marca):
    banco=conectar()
    cursor=banco.cursor()
    criar_tabela_carros()
    cursor.execute(f"SELECT * FROM carros WHERE marca={marca};")
    return cursor.fetchone()


def buscar_carro_por_modelo(modelo):
    banco=conectar()
    cursor=banco.cursor()
    criar_tabela_carros()
    cursor.execute(f"SELECT rowid, * FROM carros WHERE modelo='{modelo}';")
    return cursor.fetchall()

def deletar_carro_por_modelo(modelo):
    banco=conectar()
    cursor=banco.cursor()
    criar_tabela_carros()
    cursor.execute(f"DELETE FROM carros WHERE modelo={modelo}")
    banco.commit()
    banco.close()
def alterar_carro(marca,modelo,ano):
    banco=conectar()
    cursor=banco.cursor()
    criar_tabela_carros()
    cursor.execute(f" UPDATE carros SET marca='{marca}',modelo='{modelo}',ano='{ano}")
    banco.commit()
    banco.close()
