#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import numpy as np
import csv
import io

from cgitb import html
from PyQt5 import  uic,QtWidgets
import sqlite3
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from webapp.metodos.gauss import Gauss
from django.contrib import messages
from django.forms import ValidationError
from django.shortcuts import render
from django.urls import reverse

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ciel.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    
    
    
    
'''from django.contrib.auth import authenticate
user = authenticate(username='cieladmin', password='educacaoeachave')
if user is not None:
   return redirect('areaprofessor.html')
else:
    return redirect('login.html').setText("Login incorreto, tente novamente")
    
    def login(request):
        if request.user
        form = RegisterForm(request.POST)
    
if request.user.is_authenticated():
    return redirect('areaprofessor.html')
else:
    return redirect('login.html')
    

    
    @app.route("login/")
def index():
    return HttpResponseRedirect('\projeto-ciel\login.html')

def chama_login():
    login.html.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    
   # if usuario == "cieladmin" and senha == "educacaoeachave" :
    
   #     areaprofessor.show()
   # else :
   #     primeira_tela.label_4.setText("Dados de login incorretos!")
    
    


app=QtWidgets.QApplication([])
#login=location:login.html
#areaprofessor=location:areaprofessor.html
primeira_tela=uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)


primeira_tela.show()
app.exec()'''