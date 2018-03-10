from bs4 import BeutifulSoup

import urllib.request

url = "http://www.imbd.com/chart/top"
request = urllib.request.Request(url)
responce = urllib.request.urlopen(request)
content = responce.read()

soup = BeutifulSoup(content,"lxml")


tr = soup.findChildren("tr")

tr = iter(tr)
next(tr)

for movie in tr:
    imageUrl = movie.find('td',{'class':positionColumn}).find("img")['src'].split("@.")[0].__str__()
    title = movie.find('td', {'class': titleColumn}).find('a').contents[0]
    year = movie.find('td', {'class': titleColumn}).find('span',{'class':'secondaryInfo'}).content
    rating = movie.find('td',{'class':'ratingColumn imbdRating'}).find('storing').contents[0]
    row = title + ' - ' + year + '  ' + imageUrl + '  ' +rating
    print(row)