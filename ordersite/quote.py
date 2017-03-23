import re
from bs4 import BeautifulSoup
import requests

def get_quote():

    quote_url = "https://www.brainyquote.com/quotes_of_the_day.html"

    soup = BeautifulSoup(requests.get(quote_url).content, 'html.parser')

    my_tag = soup.find("div", {"class":"bqcpx"})

    quote = my_tag.find("a", {"title": "view quote"}).get_text()
    author = my_tag.find("a", {"title": "view author"}).get_text()
    return (quote, author)