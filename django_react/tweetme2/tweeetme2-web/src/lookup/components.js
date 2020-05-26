export function loadTweets(callback){
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