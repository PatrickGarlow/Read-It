import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
count = 1
fileName = "books_youngadult3.csv"
f = open(fileName,"w")
headers = "genre,title,author,description,image_link,num_of_pages,publish_date,audible_link,barns_and_nobel_link,google_link,amazon_link,rating,num_of_ratings\n"
genre = "youngadult"
f.write(headers)
for x in range(1,23):
    my_url = 'https://www.goodreads.com/list/show/43.Best_Young_Adult_Books'+'?page='+str(x)

    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html.parser")
    book_preview_containters = page_soup.findAll("tr",{"itemtype":"http://schema.org/Book"})


    for container in book_preview_containters:
        book_url1 = container.find("td",{"width":"5%"})
        book_url2 = book_url1.find("div",{"data-resource-type":"Book"})
        book_url3 = book_url2.a
        new_url = 'https://www.goodreads.com/' + str(book_url3['href'])
        nClient = uReq(new_url)
        book_html = nClient.read()
        nClient.close()
        book_soup = soup(book_html, "html.parser")
        book_container = book_soup.find("div",{"id":"topcol"})
        image_link = book_container.div.div.div.img['src']
        title = book_container.find("div",{"id":"metacol"}).h1.text.strip()
        author = book_container.find("div",{"id":"bookAuthors"}).find("span",{"itemprop":"author"}).div.a.span.text
        #if book_container.find("div",{"id":"descriptionContainer"}).div.find("span",{"style":"display:none"}) == None:
        #    description = book_container.find("div", {"id": "descriptionContainer"}).div.span.text
        #else:
        #    description = book_container.find("div", {"id": "descriptionContainer"}).div.find("span", {"style": "display:none"}).text
        if book_container.find("div",{"id":"details"}).find("span",{"itemprop":"numberOfPages"}) == None:
            page_number = "N/A"
        else:
            page_number = book_container.find("div",{"id":"details"}).find("span",{"itemprop":"numberOfPages"}).text.replace(" pages","")
        audible_link = book_container.find("div",{"id":"buyButtonContainer"}).find("ul",{"class":"buyButtonBar left"}).find("div",{"id":"buyDropButtonStores"}).div.findAll("a",{"class":"actionLinkLite"})[0]['href']
        audible_link = "https://www.goodreads.com" + audible_link
        barns_and_nobel_link = book_container.find("div", {"id": "buyButtonContainer"}).find("ul", {"class": "buyButtonBar left"}).find("div", {"id": "buyDropButtonStores"}).div.findAll("a", {"class": "actionLinkLite"})[1]['href']
        barns_and_nobel_link = "https://www.goodreads.com" + barns_and_nobel_link
        google_link = book_container.find("div", {"id": "buyButtonContainer"}).find("ul", {"class": "buyButtonBar left"}).find("div", {"id": "buyDropButtonStores"}).div.findAll("a", {"class": "actionLinkLite"})[3]['href']
        google_link = "https://www.goodreads.com" + google_link
        amazon_link = book_container.find("div", {"id": "buyButtonContainer"}).find("ul", {"class": "buyButtonBar left"}).li.a['href']
        amazon_link = "https://www.goodreads.com" + amazon_link
        rating = book_container.find("div",{"id":"bookMeta"}).find("span",{"itemprop":"ratingValue"}).text.strip()
        num_of_ratings = book_container.find("div",{"id":"bookMeta"}).find("a",{"class":"gr-hyperlink"}).meta.text.strip().replace("ratings","")
        #temp_string = description.replace(",","|")
        out_string = (genre + "," + title.replace(",","|") + ',' + author  + ',' +  image_link + ',' + page_number +  ',' + audible_link + ',' + barns_and_nobel_link + ',' + google_link + ',' + amazon_link + ',' + rating + ',' + num_of_ratings.replace(",","|"))
        f.write(out_string.replace('b"',''))
        print(count)
        count+=1



f.close()
print("done")