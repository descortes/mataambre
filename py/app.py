from random import randint
from flask import Flask
from flask import Response
import time

app = Flask(__name__)

@app.route('/ping', methods = ['GET'])
def ping():
	return 'pong!'

@app.route('/sleep/<int:n>', methods = ['GET'])
def sleep(n=10):
	time.sleep(n*0.001)
	return '%s' % n

@app.route('/fibo/<int:n>', methods = ['GET'])
def fibo(n):
	return '%s' % callFibo(n)

def callFibo(n):
	if n<=2:
		return 1
	return callFibo(n-1)+callFibo(n-2)
