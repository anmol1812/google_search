from googlesearch import search
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
def get_description(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    title = soup.find("meta",  property="og:description")
    return(title["content"] if title else "No meta description given")
query = "games"
for url in search(query, stop=1):
    description = get_description(url)
    print(description)
