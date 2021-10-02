import sqlite3

def conectar():
    banco=sqlite3.connect('banco.db')
    return banco
	
	
def criar_tabela_usuario():
    banco=conectar()
    cursor=banco.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(nome TEXT,cpf TEXT,idade INTERGER,salario REAL);')
    banco.commit()
    banco.close()


def inserir_usuario(nome,cpf,telefone,categoria,email):
    banco=sqlite3.connect('banco.db')
    cursor=banco.cursor()
    criar_tabela_usuario()
    cursor.execute(f"INSERT INTO usuarios VALUES('{nome}','{cpf}','{telefone}','{categoria}','{email}');")
    banco.commit()
    banco.close()


def buscar_usuario_por_cpf(cpf):
    banco=conectar()
    cursor=banco.cursor()
    criar_tabela_usuario()
    cursor.execute(f"SELECT * FROM usuarios WHERE nome='{cpf}';")
    return cursor.fetchone()

def buscar_todos_usuarios():
    banco=conectar()
    cursor=banco.cursor()
    criar_tabela_usuario()
    cursor.execute('SELECT * FROM usuarios;')
    return cursor.fetchall()

	
def deletar_usuario_por_id(cpf):
    banco=conectar()
    cursor=banco.cursor()
    criar_tabela_usuario()
    cursor.execute(f"DELETE FROM usuarios WHERE id={cpf}")
    banco.commit()
    banco.close()


def alterar_usuario(nome,cpf,idade,salario):
    banco=conectar()
    cursor=banco.cursor()
    criar_tabela_usuario()
    cursor.execute(f" UPDATE usuarios SET nome='{nome}',cpf='{cpf}',idade='{idade}',salario='{salario}', WHERE id={id}")
    banco.commit()
    banco.close()  