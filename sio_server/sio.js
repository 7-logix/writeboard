var app = require('express').createServer()
	, io = require('socket.io').listen(app);

app.listen(8080);

io.sockets.on('connection', function (socket) {
	socket.on('textchanged', function (data) {
		socket.emit('textchange', data);
	});
});