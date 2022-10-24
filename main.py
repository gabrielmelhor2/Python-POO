from database import BancoDeDados

if __name__ == "__main__":
    pass

banco = BancoDeDados()
banco.conecta()
""" banco.criar_tabelas() """
""" banco.excluir_tabela() """
""" banco.inserir_cliente("GABRIEL", "111111", "teste@gmail.COM") """
""" banco.buscar_cliente("333333") """
""" banco.buscar_cliente("222222") """
""" banco.buscar_cliente("111111") """
""" banco.remover_cliente("111111") """
""" banco.buscar_email("teste@gmail.com") """

banco.desconecta()
