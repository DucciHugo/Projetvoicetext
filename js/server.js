var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.sendFile('../index.html');
});


io.on('connection', function(socket){
  socket.on('up', function(msg){
      console.log(msg);
  });
});
 
var port = process.env.PORT || 8080; 
 
http.listen(port, function(){
  console.log('Serveur ouvert sur le port :' + port);
});