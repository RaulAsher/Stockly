import threading
from pathlib import Path
import importlib.util
import sys


from flask import Flask, render_tempalte, redirect, session, url_for, jsonify, request
import mysql.connector

app = Flask(__name__)
app.secret_key = 'a3a27266d9880ef683f05b235b73c7e1c1e3475ca2dc4514f849a15635f2c776'

# Configuração do banco de dados
thread_local = threading.local()

# Conexão com o banco de dados
def get_db_connection():
    if not hasattr(thread_local, 'connection'):
        thread_local.connection = mysql.connector.connect(
            host='localhost',
            user='flaskuser',
            password='root',
            database='stockly'
        )
    return thread_local.connection


