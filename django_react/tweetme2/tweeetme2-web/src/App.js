import React, {useEffect, useState  } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  // dzieki temu mozemy z tego kozystac w dalszej lini kodu
  // troche def zmiennej
  // np: const [tweets, setTweets] = useState([{content: 123}])
  const [tweets, setTweets] = useState([])

  useEffect(()=>{
    // do lookup for tweets
    const tweetItems = [{content: 123}, {content: "dupa"}]
    setTweets(tweetItems)
  }, [])


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          {tweets.map((tweet, index)=>{
            return <li>{tweet.content}</li>
          })}
        </p>
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
