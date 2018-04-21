from flask import Flask

mataambre = Flask(__name__)

@mataambre.route('/hola/<int:nombre>')

def hola(nombre):
	return 'Hola Mundo '+ str(nombre) + '\n'