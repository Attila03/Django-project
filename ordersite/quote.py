from bs4 import BeautifulSoup
import requests

def get_quote():

    quote_url = "https://www.brainyquote.com/quotes_of_the_day.html"

    try:
        quote_page = requests.get(quote_url)
    except:
        return ("To begin, begin", "Anonymous")

    soup = BeautifulSoup(quote_page.content, 'html.parser')

    my_tag = soup.find("div", {"class":"bqcpx"})

    quote = my_tag.find("a", {"title": "view quote"}).get_text()
    author = my_tag.find("a", {"title": "view author"}).get_text()
    return (quote, author)