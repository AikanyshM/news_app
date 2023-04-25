from django.shortcuts import render
import requests
API_KEY = '8339226839d94928bd4171fb3a213080'


def home(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)

    context = {
        'data': data
    }
    return render(request, 'news_api/home.html', context)