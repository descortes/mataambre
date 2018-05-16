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
	return '%s' % n*0.001

@app.route('/fibo/<int:n>', methods = ['GET'])
def fibo(n):
	return '%s' % callFibo(n)

def callFibo(n):
	if n<=2:
		return 1
	return calFib(n-1)+calFib(n-2)
