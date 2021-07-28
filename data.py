import sqlite3

CREATE_TABLE = "create table produto(cod integer, nome text, descricao text, quantidade integer)"
INSERT_PRODUTO = "insert into produto (cod, nome, descricao, quantidade) values (?, ?, ?, ?);"
BUSCA_PRODUTO_POR_NOME = "select * from produto where nome = ?;"

def connect():
    return sqlite3.connect("produto.db")

#função cria tabela
def create(conexao):
    with conexao:
        conexao.execute(CREATE_TABLE)

#função inserir
def cadastrar(conexao, cod, nome, descricao, quantidade):
    with conexao:
        conexao.execute(INSERT_PRODUTO,( cod, nome, descricao, quantidade))

#função busca por nome
def busca_nome(conexao, nome):
    with conexao:
        return conexao.execute(BUSCA_PRODUTO_POR_NOME, (nome, )).fetchall()