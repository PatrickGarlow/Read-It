import urllib
import requests
from bs4 import BeautifulSoup
import csv
with open('_books_sports.csv',newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

fileName = "sports.csv"
f = open(fileName,"w", encoding='utf-8')

headers = "google\n"
f.write(headers)


# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
count = 0
for x in range(0,322):

    book = data[x]
    count += 1
    query = book[1] + ' book barnes and noble'
    query = query.replace(' ', '%20').replace("|",",")
    URL = 'https://google.com/search?q='+query




    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)

    soup = BeautifulSoup(resp.content, "html.parser")
    if soup.find('div', {"id":"search"}).div.div.div.div.div == None:
        g = "N/A\n"
    else:
        g = soup.find('div', {"id":"search"}).div.div.div.div.div.a['href'] + "\n"

    f.write(g)

    print(count)
f.close()
