from modules.scrape import getData
from modules.prompt import getPrompt
from modules.gpt import getResponse
import pandas

class company:
    def __init__(self, name, url):
        self.name = name
        self.url = url

def main():
        
    data = pandas.read_csv("./dataset/returns.csv")
    for index, row in data.iterrows():
        print(row['name'])
        print(row['url'])

    ## get objects from csv here and call export
    ##c = company('ford', 'dfkhfolfke')
    ##print(c.url)


main()