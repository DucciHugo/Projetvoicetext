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

io.sockets.on('connection', (socket) => {
    console.log('Utilisateur '+socket.id+' connecté');
    socket.on('disconnect', () => {
      console.log('Utilisateur '+socket.id+' deconnecté');
    });

    socket.on('msg-'+socket.id, (msg) => {
        console.log('Mot : ' + msg);
        io.emit('msg-'+socket.id, msg);
          Axios.post('http://localhost:5000/insert',{
            mot:msg
          })
      });
    socket.on('python-'+socket.id,(data) => {
         console.log("Chargement du script python pour "+socket.id)
         const py = spawn('python3',['vosk/micro.py'])
         py.stdout.on('data',(data)=>{
            console.log(data.toString())
            data=data.toString();
            data=data.split(',');
            io.emit('msg-'+socket.id,data);
            Axios.post('http://localhost:5000/insert',{
              mot:data[1]
            })
         })
         py.stderr.on('data',(data)=>{
            console.error(`stderr: ${data}`);

            if(data.toString().includes("PortAudioError")){
             io.emit('msg-'+socket.id,["Erreur du micro, veullez réessayer : ","Vérifier le branchement du micro"]);
           }
         })
     });
  });

  
server.listen(5000, () => {
  console.log('listening on *:5000');
});
