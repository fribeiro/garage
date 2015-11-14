var express = require('express'),
http = require('http'),
path = require('path'),
amqp = require('amqplib');
var when = require('when');

var app = express();

app.get('/main', function (req, res) {
  if(req.query.token === '3e46ce0d-39b3-4291-99f2-a624b40246b7'){
    amqp.connect('amqp://garage:viviana1!@45.55.154.178').then(function(conn) {
      return when(conn.createChannel().then(function(ch) {
        var q = 'door';
        var msg = 'main';

        var ok = ch.assertQueue(q, {durable: false});
      
        return ok.then(function(_qok) {
          ch.sendToQueue(q, new Buffer(msg));
          return ch.close();
        });
      })).ensure(function() { conn.close(); });
    }).then(null, console.warn);
    res.send('done!');
  } else {
    res.send(401,'failed!');
  }
});

app.get('/side', function (req, res) {
  if(req.query.token === '3e46ce0d-39b3-4291-99f2-a624b40246b7'){
    amqp.connect('amqp://garage:viviana1!@45.55.154.178').then(function(conn) {
      return when(conn.createChannel().then(function(ch) {
        var q = 'door';
        var msg = 'side';

        var ok = ch.assertQueue(q, {durable: false});
      
        return ok.then(function(_qok) {
          ch.sendToQueue(q, new Buffer(msg));
          return ch.close();
        });
      })).ensure(function() { conn.close(); });
    }).then(null, console.warn);
    res.send('done!');
  } else {
    res.send(401,'failed!');
  }
});

var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
