from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.http import is_safe_url
from django.conf import settings

from .models import Tweet
from .forms import TweetForm

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        if next_url != None and is_safe_url(next_url, settings.ALLOWED_HOSTS):
            return redirect(next_url)
        form=TweetForm()
    return render(request, 'components/form.html', context={"form":form})

def home_view(request, *args, **kwargs):
    return render(request, "home.html")

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes": 1} for x in qs]
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