var app = require('express')();
var http = require('http');
var server = http.Server(app)
var io = require('socket.io')(server);
var port = process.env.PORT || 3000;

const URL_ROBO = "http://localhost:5000/responder/";

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

getResposta = (msg) => {
  let dados = "";

  http.get(URL_ROBO + msg, (resposta) => {
    resposta.on("data", (pedaco) => {
      dados += pedaco;
    });

    resposta.on("end", () => {
      const resposta = JSON.parse(dados);
      if (resposta.confianca >= 0.6){
        io.emit("chat message", "RodôBot: "+ resposta.resposta);
      } else {
        io.emit("chat message", "RodôBot: Ops! Ainda não sei como responder isso, posso te ajudar em outra coisa?");
      }
    })
  })
}

io.on('connection', function (socket) {
  socket.on('chat message', function (msg) {
    io.emit('chat message', "Você: " + msg);
    getResposta(msg);
  });
});

server.listen(port, function () {
  console.log('listening on *:' + port);
});
