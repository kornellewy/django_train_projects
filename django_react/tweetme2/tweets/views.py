from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Tweet


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html")

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data= {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)
    

def tweet_detail_view(request, tweet_id):
    obj = get_object_or_404(Tweet, pk=tweet_id)
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        data = {
                "id": tweet_id,
                "content": obj.content,
                }
    except :
        data['message'] = "not found"
        status = 404
    return JsonResponse(data, status = status)