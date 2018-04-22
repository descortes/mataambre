from flask import Flask
from flask import Response

mataambre = Flask(__name__)

@mataambre.route('/cortesdecarne/mataambre', methods = ['GET'])
def getmataambre():
	return 'mataambre \n'