from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tweet
from django.shortcuts import get_object_or_404

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse('HUJ')

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