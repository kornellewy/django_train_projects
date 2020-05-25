import React, {useEffect, useState  } from 'react';
import logo from './logo.svg';
import './App.css';

function loadTweets(callback){
  const xhr = new XMLHttpRequest() //const to deklaracja typuz zmienej, new nowy obiekt
  const method = 'GET' // Zamiast post
  const url = 'http://localhost:8000/api/tweets'
  const responseType = "json"
  // ustawiamy typ odpowiedzi
  xhr.responseType = responseType
  // open requset with this method and that url
  xhr.open(method, url)
  // jak skonczymy sie wczytywac strona to to rb
  xhr.onload = function() {
      // odpalamy fun z callbacka
      callback(xhr.response, xhr.status)
  }
  xhr.onerror= function (e){
    console.log(e)
    callback({"message": "The request was an error"}, 400)
  }
  xhr.send()
}

function Tweet(props){
  const {tweet} = props
  const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
  return (<div className={className}>
    <p>{tweet.id} - {tweet.content}</p>
  </div>)
}

function App() {
  // dzieki temu mozemy z tego kozystac w dalszej lini kodu
  // troche def zmiennej
  // np: const [tweets, setTweets] = useState([{content: 123}])
  const [tweets, setTweets] = useState([])
  

  useEffect(()=>{
    // do lookup for tweets
    const myCallBack = (response, status) => {
      console.log(response, status)
      if (status===200){
        setTweets(response)
      }
    }
    loadTweets(myCallBack)
  }, [])

  // definicja call


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <div>
          {tweets.map((item, index)=>{
            return <Tweet tweet={item} className='my-5 py-5 border bg-white text-dark' 
            key = {`${index}-{item.id}`}/>
          })}
        </div>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
