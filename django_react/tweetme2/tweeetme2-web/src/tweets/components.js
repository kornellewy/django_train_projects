import React, {useEffect, useState  } from 'react';

// podwujna kropka znaczy ze idziemy 2 lvl wyrzej 
import {loadTweets} from '../lookup'


export function TweetsList(props){
  const [tweets, setTweets] = useState([])
  
  useEffect(()=>{
    // do lookup for tweets
    const myCallBack = (response, status) => {
      // console.log(response, status)
      if (status===200){
        setTweets(response)
      }
    }
    loadTweets(myCallBack)
  }, [])
  return tweets.map((item, index)=>{
    return <Tweet tweet={item} className='my-5 py-5 border bg-white text-dark' 
    key = {`${index}-{item.id}`}/>
  })
}

export function TweetsComponent(props){
  const handleSubmit = (event) => {
    event.preventDefault()
    console.log(event)
  }
  return <div className={props.className}>
    <div className='col-12 mb-3'>
      <form onSubmit={handleSubmit}>
        <textarea className="form-control" name='tweet'>

        </textarea>
        <button type="submit" className = "btn btn-primary my-3">Tweet</button>
      </form>
    </div>
  <TweetsList />
  </div>
}

export function ActionBtn(props){
    const {tweet, action} = props
    const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0)
    const[userLike, setUserLike] = useState(tweet.userLike === true ? true : false)
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    const actionDisplay = action.display ? action.display : "Action"
    
    const handleClick = (event) =>{
      event.preventDefault()
      if (action.type === "like"){
        if (userLike === true){
          setLikes(likes-1)
          setUserLike(false)
        }else {
          setLikes(likes+1)
          setUserLike(true)
        }
        
      }
    }
    const display = action.type === "like" ? `${likes} ${actionDisplay}` : actionDisplay
    return <button className={className} onClick={handleClick}>{display}</button>
  }
  
export function Tweet(props){
    const {tweet} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return (<div className={className}>
      <p>{tweet.id} - {tweet.content}</p>
      <div className='btn btn-group'>
        <ActionBtn tweet={tweet} action={{type:"like", display: "Likes"}}/>
        <ActionBtn tweet={tweet} action={{type:"unlike", display: "Unlike"}}/>
        <ActionBtn tweet={tweet} action={{type:"retweet", display: "Retweet"}}/>
      </div>
    </div>)
  }