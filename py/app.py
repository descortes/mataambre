from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/cortesdecarne/mataambre', methods = ['GET'])
def getmataambre():
	return 'mataambre \n'