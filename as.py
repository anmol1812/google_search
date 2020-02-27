# import required packages
from googlesearch import search
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
# define connection with the browser and parse html code that show in the developer tools
def get_description(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    title = soup.find("meta",  property="og:description")
    return(title["content"] if title else "No meta description given")
# take a search query
query = "gamezop"
# get text description for the query 
for url in search(query, stop=1):
    description = get_description(url)
    print(description)
