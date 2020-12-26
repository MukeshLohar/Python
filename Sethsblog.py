#each time you run this code, it will create a notepad with sets
#
import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from datetime import datetime
r = requests.get("https://seths.blog/")

soup = BeautifulSoup(r.text, 'lxml')
time_now = datetime.today()

paragraphs = []

articles_in_seth ={}
def Checking_date(input_date):
    input_date = datetime.strptime(input_date, '%B %d, %Y')
    time = datetime.today()
    time_delta = time - input_date
    if time_delta.days >= 10:
        # print(f'there was no post before {time_delta}')
        return False
    else:
        # print(f'this was {time_delta.days} days old post')
        return True

for article in soup.find_all('div', class_='post'):
    #  print(article.prettify())
    article_date = article.find('span', class_='date').text
    # print("|"*100)
    if not Checking_date(article_date):
        break
    else:
        headline = article.h2.text
        paragraphs = []
        for article_content in article.find_all('p', class_=None):
            paragraphs.append(article_content.text)
          
        articles_in_seth[headline] = '\n'.join(paragraphs)


with open("news.txt" , 'w') as file : #provide the file directory path here : format  as follows open(filepathalongwithextension , 'w')
    for key,value in articles_in_seth.items() :
        file.write("-"*len(key))
        file.write('\n')
        file.write(key)
        file.write('\n')
        file.write("-"*len(key))
        file.write('\n')
        file.write(''.join(value))
        file.write('\n')
        
        file.write('That is all for today!')
        file.write('\n')
