const express = require('express');
const app = express();

app.get('/ping', (req, res) => {
	res.send('pong!');
});

app.get('/fibo/:numb', (req, res) => {
	res.send('' + fibo(req.params.numb));
});

app.get('/sleep/:numb', (req, res) => {
	setTimeout(function() {res.send(''+req.params.numb)}, req.params.numb);
});

function fibo(n) {
	if (n>1)
		return fibo(n-1) + fibo(n-2);
	return n;
}

const PORT = 3000;

app.listen(PORT, () => console.log('Escuchando en el puerto' + PORT));
