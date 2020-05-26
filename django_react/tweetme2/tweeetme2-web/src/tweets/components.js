import React, {useEffect, useState  } from 'react';

// podwujna kropka znaczy ze idziemy 2 lvl wyrzej 
import {loadTweets} from '../lookup'


export function TweetsList(props) {
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

export function ActionBtn(props){
    const {tweet, action} = props
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    return action.type === "like" ? <button className={className}>{tweet.likes} Likes</button> : null
  }
  
export function Tweet(props){
    const {tweet} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return (<div className={className}>
      <p>{tweet.id} - {tweet.content}</p>
      <div className='btn btn-group'>
        <ActionBtn tweet={tweet} action={{type:"like"}}/>
        <ActionBtn tweet={tweet} action={{type:"unlike"}}/>
      </div>
    </div>)
  }