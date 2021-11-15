const express = require('express')
const bodyParser = require('body-parser');
const cors = require('cors')
const app = express()
const mysql = require('mysql')

const db = mysql.createPool({
    host:"localhost",
    user:"root",
    password:"",
    database:"dbvoice",
})
app.use(cors())
app.use(express.json())
app.use(bodyParser.urlencoded({extended:true}))


app.get('/get', (req,res) =>{
    const sqlSelect = "SELECT * FROM motscles ";
    db.query(sqlSelect, (err,result) =>{
        res.send(result)
    })
})

app.post("/insert",(req,res)=>{
    const mot = req.body.mot
    const sqlInsert = "INSERT INTO motscles (mot) VALUES (?)";
    db.query(sqlInsert, [mot], (err,result) =>{
        console.log(result)
    })
})


app.listen(3001,() =>{
    console.log('Running on port 3001')
})