import requests
from send_email import send_email


api_key = '9518b161a9884fd7bb42212ccab291bf'
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=9518b161a9884fd7bb42212ccab291bf"

# Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if (article["description"] is not None) and (article["title"] is not None):
        body = body + article["title"] + "\n"\
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
