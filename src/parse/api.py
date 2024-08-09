import requests


def request_get():

    url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-07-08&sortBy=publishedAt&apiKey=cefee91e87f34a25bdf48c668c38194e'

    response = requests.get(url)
    return response.json()



