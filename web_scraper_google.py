import urllib
import requests
from bs4 import BeautifulSoup
import csv
with open('_books_youngadult.csv',newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

fileName = "youngadult.csv"
f = open(fileName,"w", encoding='utf-8')

headers = "google\n"
f.write(headers)


# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
count = 0
for x in range(0,2044):

    book = data[x]
    count += 1
    query = book[1] + ' Book Google'
    query = query.replace(' ', '%20').replace("|",",")
    URL = 'https://google.com/search?q='+query




    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)

    soup = BeautifulSoup(resp.content, "html.parser")
    g = soup.find('div', {"class":"r"})
    if g == None:
        f.write("N/A\n")
    else:
        text = g.a['href']+ '\n'
        f.write(text)
    print(count)
f.close()
