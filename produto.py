import data
import sqlite3
from PyQt5 import uic, QtWidgets

#função de cadastro
def menuCad():
    #controle de tela
    tela.close()
    tela_cad.show()

def cadastrar():
    #conexao com o banco de dados
    conexao = data.connect()
    #data.create(conexao)

    #recebendo informações
    cod = tela_cad.lineEdit_Cod.text()
    nome = tela_cad.lineEdit_Nome.text()
    descricao = tela_cad.lineEdit_Desc.text()
    quantidade = tela_cad.lineEdit_Quant.text()

    #inserindo na base
    data.cadastrar(conexao, cod, nome, descricao, quantidade)

    #limpando os botões
    tela_cad.lineEdit_Cod.setText("")
    tela_cad.lineEdit_Nome.setText("")
    tela_cad.lineEdit_Desc.setText("")
    tela_cad.lineEdit_Quant.setText("")
    limpeza()

#confirmando o cadastro através de uma mensagem    
def cadastrado():
    tela_cad.label_Cadastrado.setText("Produto cadastrado com sucesso!")

def limpeza():
    banco = sqlite3.connect("produto.db")
    cursor = banco.cursor()
    cursor.execute("""
    delete from produto 
    where nome is NULL
    or nome = ""
    """)
    cursor.execute("""
    delete from produto 
    where cod is NULL
    or cod = ""
    """)
    banco.commit()
    banco.close()

def produtos():
    tela.close()
    tela_prod.show()
    banco = sqlite3.connect("produto.db")
    cursor = banco.cursor()
    cursor.execute("select * from produto order by nome;")
    lidos = cursor.fetchall()

    #criando a tabela na interface
    tela_prod.tableWidget.setRowCount(len(lidos))
    tela_prod.tableWidget.setColumnCount(4)

    for i in range(0, len(lidos)):
        for j in range(0, 4):
            tela_prod.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
    
    limpeza()

def menuBusca():
    tela.close()
    tela_busca.show()

def busca_cod():
    banco = sqlite3.connect("produto.db")
    cursor = banco.cursor()

    cod = tela_busca.lineEdit_Cod.text()
   
    cursor.execute("select * from produto where cod = ?", (cod, ))
    
    lidos = cursor.fetchall()
    tela_resultado.tableWidget.setRowCount(len(lidos))
    tela_resultado.tableWidget.setColumnCount(4)

    for i in range(0, len(lidos)):
        for j in range(0, 4):
            tela_resultado.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
    banco.close()

def busca_nome():
    banco = sqlite3.connect("produto.db")
    cursor = banco.cursor()

    nome = tela_busca.lineEdit_Nome.text()
   
    cursor.execute("select * from produto where nome = ?", (nome, ))
    
    lidos = cursor.fetchall()
    tela_resultado.tableWidget.setRowCount(len(lidos))
    tela_resultado.tableWidget.setColumnCount(4)

    for i in range(0, len(lidos)):
        for j in range(0, 4):
            tela_resultado.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
    banco.close()
    
def resultado():
    tela_resultado.show()
    tela_busca.lineEdit_Nome.setText("")
    tela_busca.lineEdit_Cod.setText("")
    

def menuExcluir():
    tela.close()
    tela_excluir.show()

def excluir_cod():
    banco = sqlite3.connect("produto.db")
    cursor = banco.cursor()
    cod = tela_excluir.lineEdit_Cod.text()
    cursor.execute("delete from produto where cod = ?", (cod, ))
    banco.commit()
    banco.close()

def excluir_nome():
    banco = sqlite3.connect("produto.db")
    cursor = banco.cursor()
    nome = tela_excluir.lineEdit_Nome.text()
    cursor.execute("delete from produto where nome = ?", (nome, ))
    banco.commit()
    banco.close()

def excluido():
    tela_excluir.label_Excluido.setText("Produto excluído com sucesso!")
    tela_excluir.lineEdit_Nome.setText("")
    tela_excluir.lineEdit_Cod.setText("")


#função menu
def menu():
    #limpando para evitar lixo ao cancelar
    tela_cad.lineEdit_Cod.setText("")
    tela_cad.lineEdit_Nome.setText("")
    tela_cad.lineEdit_Desc.setText("")
    tela_cad.lineEdit_Quant.setText("")
    tela_busca.lineEdit_Nome.setText("")
    tela_busca.lineEdit_Cod.setText("")
    tela_excluir.lineEdit_Nome.setText("")
    tela_excluir.lineEdit_Cod.setText("")

    #fechando as telas que podem estar abertas
    tela_cad.close()
    tela_prod.close()
    tela_busca.close()
    tela_resultado.close()
    tela_excluir.close()

    #abrindo a tela principal
    tela.show()

    #excluindo dados vazios do banco
    limpeza()

app = QtWidgets.QApplication([])
tela = uic.loadUi("menu.ui")
tela_cad = uic.loadUi("cadastrar.ui")
tela_prod = uic.loadUi("produtos.ui")
tela_busca = uic.loadUi("busca.ui")
tela_resultado = uic.loadUi("resultado.ui")
tela_excluir = uic.loadUi("excluir.ui")

#botões

#tela menu
tela.pushButton_MCad.clicked.connect(menuCad)
tela.pushButton_MPro.clicked.connect(produtos)
tela.pushButton_MBus.clicked.connect(menuBusca)
tela.pushButton_MExc.clicked.connect(menuExcluir)


#tela cadastro
tela_cad.pushButton_Cadastrar.clicked.connect(cadastrar)
tela_cad.pushButton_Cadastrar.clicked.connect(cadastrado)
tela_cad.pushButton_Cancelar.clicked.connect(menu)

#tela produtos
tela_prod.pushButton_Cancelar.clicked.connect(menu)

#tela busca
tela_busca.pushButton_ProCod.clicked.connect(busca_cod)
tela_busca.pushButton_ProCod.clicked.connect(resultado)
tela_busca.pushButton_ProNome.clicked.connect(busca_nome)
tela_busca.pushButton_ProNome.clicked.connect(resultado)
tela_busca.pushButton_Cancelar.clicked.connect(menu)
tela_resultado.pushButton_Cancelar.clicked.connect(menu)

#tela de exclusão
tela_excluir.pushButton_ExcCod.clicked.connect(excluir_cod)
tela_excluir.pushButton_ExcCod.clicked.connect(excluido)
tela_excluir.pushButton_ExcNome.clicked.connect(excluir_nome)
tela_excluir.pushButton_ExcNome.clicked.connect(excluido)
tela_excluir.pushButton_Cancelar.clicked.connect(menu)

tela.show()
app.exec()