import React,{useState, useEffect} from "react"
import './App.css';
import Axios from "axios"
function App() {

  const [mot,setMot] =useState('');
  const [motGet, setMotGet] = useState([]);
  useEffect(()=>{
    Axios.get('http://localhost:3001/get').then((response)=>{
      setMotGet(response.data)
    })
  },[])
  
  const submitMot = () =>{
    Axios.post('http://localhost:3001/insert',{
      mot:mot
    }).then(()=>{
      alert('success')
    })
  };

  return (
    <div className="App">
      <h1>Test</h1>
      <div className="form">
        <label>Mot clef:</label>
        <input type="text" name="motClef" onChange={(e)=>{
          setMot(e.target.value)
        }}/> 
        <button onClick={submitMot}>Envoyer en BDD</button>
        <h1>Mot clef </h1>
        {motGet.map((value)=>{
          return <h1>N°{value.id} - {value.mot}</h1>
        })}
      </div>
    </div>
  );
}

export default App;
