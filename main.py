import requests
from send_email import send_email

api_key = '9518b161a9884fd7bb42212ccab291bf'
url = ("https://newsapi.org/v2/everything?q=tesla"
       "&from=2025-06-15&sortBy=publishedAt&apiKey=9518b161a9884fd7bb42212ccab291bf")

# Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
