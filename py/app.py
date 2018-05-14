from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/saludo/hola', methods = ['GET'])
def getmataambre():
	return 'mundo \n'