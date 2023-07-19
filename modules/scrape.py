import requests
import re
from bs4 import BeautifulSoup

def getData(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    separator = r'\s+'
    ## try here
    text = soup.text
    text = re.sub(separator, ' ', ''.join(text))
    return text + '\n'