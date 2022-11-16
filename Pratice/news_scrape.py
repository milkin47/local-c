import requests

def get_req():
    url = f"https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-5-01&to=2022-5-02&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c"
    r = requests.get(url)
    print(r)
    content = r.json()
    articles = content['articles']
    for art in articles:
        print("Title")
        print("\n", art['title'])
get_req()







