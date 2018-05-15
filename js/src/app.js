const express = require('express');
const app = express();

app.get('/hola', (req, res) => {
	res.send('Hola Mundo!');
});

app.get('/hola/:id', (req, res) => {
	res.send('Hola Mundo! ' + req.params.id);
});

app.get('/fibo/:numb', (req, res) => {
	var numb = req.params.numb || 1;
	res.send('' + fibo(numb));
});

app.get('/sleep/:numb', (req, res) => {
	var numb = req.params.numb || 5;
	setTimeout(function() {res.send(''+numb)}, numb*1000);
});

app.get('/random/:numb', (req, res) => {
	var numb = req.params.numb || 23;
	res.send(random(numb));
});

function random(min, max) {
	return Math.floor(Math.random() * (max - min)) + min;
}

function fibo(n) {
	if (n>1)
		return fibo(n-1) + fibo(n-2);
	return n;
}

const PORT = 3000;

app.listen(PORT, () => console.log('Escuchando en el puerto' + PORT));
