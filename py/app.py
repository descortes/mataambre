from random import randint
from flask import Flask
from flask import Response
import time

app = Flask(__name__)

@app.route('/ping', methods = ['GET'])
def getmataambre():
	return 'pong!'

@app.route('/sleep/<int:n>', methods = ['GET'])
def sleep(n=10):
	time.sleep(n)
	return 'Sleep: %s seconds.' % n

@app.route('/fibo/<int:n>', methods = ['GET'])
def getFibo(n):
	return '%s' % calFib(n)

def calFib(n):
	if n<=2:
		return 1
	return calFib(n-1)+calFib(n-2)