from cgitb import html
from PyQt5 import  uic,QtWidgets
import sqlite3


@app.route("login/")
def index():
    return HttpResponseRedirect('\projeto-ciel\login.html')

def chama_segunda_tela():
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    if usuario == "cieladmin" and senha == "educacaoeachave" :
    
        areaprofessor.show()
    else :
        primeira_tela.label_4.setText("Dados de login incorretos!")
    


    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+login+"','"+senha+"')")

            banco.commit() 
            banco.close()
            tela_cadastro.label.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cadastro.label.setText("As senhas digitadas estão diferentes")
    

    


app=QtWidgets.QApplication([])
#login=location:login.html
#areaprofessor=location:areaprofessor.html
primeira_tela=uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)


primeira_tela.show()
app.exec()