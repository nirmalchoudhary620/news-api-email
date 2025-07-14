import requests

api_key = '9518b161a9884fd7bb42212ccab291bf'
url = ("https://newsapi.org/v2/everything?q=tesla&from=2025-06-14&sortBy=publishedAt"
       "&apiKey=9518b161a9884fd7bb42212ccab291bf")

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
