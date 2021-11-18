const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
const bodyParser = require('body-parser');
const cors = require('cors')
const mysql = require('mysql')
const Axios = require("axios")
const { spawn } = require('child_process');

// const db = mysql.createPool({
//   host:"localhost",
//   user:"root",
//   password:"",
//   database:"dbvoice",
// })
const db = mysql.createPool({
  host:"localhost",
  user:"admin",
  password:"admin",
  database:"dbvoice",
})
app.use(express.static(__dirname));


app.use(cors())
app.use(express.json())
app.use(bodyParser.urlencoded({extended:true}))

app.get('/get', (req,res) =>{
  const sqlSelect = "SELECT * FROM motscles ";
  db.query(sqlSelect, (err,result) =>{
      res.send(result)
  }).catch((err)=>{
    console.log(err)
  })
})

app.post("/insert",(req,res)=>{
  const mot = req.body.mot
  const sqlInsert = "INSERT INTO motscles (mot) VALUES (?)";
  db.query(sqlInsert, [mot], (err,result) =>{
      console.log(result)
      if (err) { 
        console.log(err); 
      }
  })

})

io.on('connection', (socket) => {
    console.log('a user connected');
    socket.on('disconnect', () => {
      console.log('user disconnected');
    });

    socket.on('msg', (msg) => {
        console.log('Mot : ' + msg);
        io.emit('msg', msg);
          Axios.post('http://localhost:5000/insert',{
            mot:msg
          })
      });
    socket.on('python',(data) => {
         console.log("Chargement du script python pour "+socket.id)
         const py = spawn('python3',['vosk/micro.py'])
         py.stdout.on('data',(data)=>{
            console.log(data.toString())
            data=data.toString();
            data=data.split(',');
            //var firstIndex = data.indexOf("$");
            //var lastIndex = data.lastIndexOf("$");
            //var msg = String(data).substr(firstIndex+1, lastIndex-firstIndex-1);
            io.emit('msg',data);
         })
         py.stderr.on('data',(data)=>{
            console.error(`stderr: ${data}`);
           // io.emit('msg',data);
         })
     });
  });

  
server.listen(5000, () => {
  console.log('listening on *:5000');
});
