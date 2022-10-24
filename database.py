import sqlite3


class BancoDeDados:
    """ Classe que representa o banco de dados """

    def __init__(self, nome='banco.db'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        """Conecta passando o nome do arquivo"""
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        """Desconecta do banco"""
        try:
            self.conexao.close()
        except AttributeError:
            pass

    def criar_tabelas(self):
        """Cria as tabelas do banco"""
        try:
            cursor = self.conexao.cursor()

            cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes (
					id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	                nome VARCHAR(50) NOT NULL,
                    senha VARCHAR(20) NOT NULL,
                    cpf VARCHAR(11) UNIQUE NOT NULL,
	                email VARCHAR(50) NOT NULL
			);
			""")
        except AttributeError:
            print('Faça a conexão do banco antes de criar as tabelas.')

    def excluir_tabela(self):
        try:
            cursor = self.conexao.cursor()

            cursor.execute("""DROP TABLE email""")
        except AttributeError:
            print('Faça a conexão do banco antes de deletar clientes.')

    def inserir_cliente(self, nome, cpf, email):
        """Insere cliente no banco"""
        try:
            cursor = self.conexao.cursor()

            try:
                cursor.execute(""" INSERT INTO clientes (nome, cpf, email) VALUES (?,?,?)
                """, (nome, cpf, email))
                print("Cliente %s foi cadastrado com sucesso" % nome)
            except sqlite3.IntegrityError:
                print('O cpf %s já existe!' % cpf)
            self.conexao.commit()

        except AttributeError:
            print('Faça a conexão do banco antes de inserir clientes.')

    def buscar_cliente(self, cpf):
        """Busca um cliente pelo cpf"""
        try:
            cursor = self.conexao.cursor()

            # obtém todos os dados
            cursor.execute("""SELECT * FROM clientes;""")

            for linha in cursor.fetchall():
                if linha[2] == cpf:
                    print('Cliente %s encontrado.' % linha[1])
                    return linha[1]
                    break
        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes.')

    def remover_cliente(self, cpf):
        """remover um cliente pelo cpf"""
        try:
            cursor = self.conexao.cursor()

            # BUSCAR O CPF INSERIDO
            cli = self.buscar_todos_clientes()
            cursor.execute(
                """DELETE FROM clientes WHERE cpf = %d""" % int(cpf))
            self.conexao.commit()
            if self.buscar_cliente(cpf) != 'None':
                print('O cliente %s foi removido com sucesso.' % cli)
            else:
                print('O CPF %s nao esta cadastrado no banco.' % cpf)

        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes.')

    def buscar_email(self, email):
        """Busca um cliente pelo cpf"""
        try:
            cursor = self.conexao.cursor()

            # obtém todos os dados
            cursor.execute("""SELECT * FROM clientes;""")

            for linha in cursor.fetchall():
                if linha[3] == email:
                    return True
                else:
                    return False
        except AttributeError:
            print('Faça a conexão do banco antes de buscar clientes.')
