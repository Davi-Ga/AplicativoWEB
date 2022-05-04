from banco import app
from flask import render_template
from banco.models import Banco,Agencia

@app.route('/')
def home_page():
    return render_template('index.html')    

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

