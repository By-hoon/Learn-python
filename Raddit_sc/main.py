import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "golang",
    "css",
    "flutter",
    "rust",
    "django"
]


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html", subreddits=subreddits)


@app.route("/read", methods=['POST', 'GET'])
def read():
    temp = []
    lang = ''
    for sd in subreddits:
        if request.args.get(sd) == sd:
            lang = (f"{lang}r/{sd} ")
            result = requests.get(
                f"https://www.reddit.com/r/{sd}/top/?t=month")
            soup = BeautifulSoup(result.text, 'html.parser')
            main = soup.find_all("div", {"class": "_1oQyIsiPHYt6nx7VOmd1sz"})
            for mi in main:
                try:
                    one = mi.find("div", {"class": "_1poyrkZ7g36PawDueRza-J"})
                    two = one.find("div", {"class": "_2FCtq-QzlfuN-SwVMUZMM3"})
                    three = two.find("div", {"class": "y8HYJ-y_lTUHkQIc1mdCq"})
                    address = three.find("a")
                    href = (f"https://www.reddit.com/{address['href']}")
                    title1 = three.find("div")
                    title2 = title1.find("h3")
                    vote1 = mi.find(
                        "div", {"class": "_23h0-EcaBUorIHC-JZyh6J"})
                    vote2 = vote1.find("div")
                    vote = vote2.find("div")
                    temp.append(
                        {'address': href, 'title': title2.text, 'vote': vote.text, 'lang': sd})
                except:
                    print(sd)
                    pass
    return render_template("read.html", lang=lang, rd=temp)


app.run(host="127.0.0.1", port=9000)
