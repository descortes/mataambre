const express = require('express');

const app = express();

app.get('/hola', (req, res) => {
	res.send('Hola Mundo!');
});

app.get('/hola/:id', (req, res) => {
	res.send('Hola Mundo! ' + req.params.id);
});

const PORT = 3000;

app.listen(PORT, () => console.log('Escuchando en el puerto' + PORT));
