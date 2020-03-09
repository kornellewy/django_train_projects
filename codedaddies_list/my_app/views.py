from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    # ver 1
    # # wyjmujemy z metody post z playholdera search co zostalo wpisane
    # search = request.POST.get('search')
    # # print(search)
    # # tworze zmmnienna do wysysylania do html
    # staff_for_frontend = {
    #     'search': search,
    # }
    # # tworze html i wysylam do niego dane do wyswietlenia
    # return render(request, 'my_app/new_search.html', staff_for_frontend)
    # wyjmujemy z metody post z playholdera search co zostalo wpisane
    # ver 2
    # dostajemy od html
    search = request.POST.get('search')
    # twozymy obiekt w DB
    models.Search.objects.create(search=search)
    # robimy dobre query z + zamiast ' '
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    # dostajemy odpowiedzi  z neta
    response = requests.get(final_url)
    data = response.text
    # zaba w web scraping
    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    final_postings = []
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        final_postings.append((post_title, post_url, post_price, post_image_url))

    # tworze zmmnienna do wysysylania do html
    staff_for_frontend = {
        'search': search,
        'final_postings': final_postings,
    }
    # tworze html i wysylam do niego dane do wyswietlenia
    return render(request, 'my_app/new_search.html', staff_for_frontend)
