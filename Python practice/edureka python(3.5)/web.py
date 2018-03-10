from bs4 import BeautifulSoup



import urllib.request

url = "view-source:http://www.imdb.com/chart/top"
request = urllib.request.Request(url)
responce = urllib.request.urlopen(request)
content = responce.read()

soup = BeautifulSoup(content,"lxml")


tr = soup.findChildren("tr")

tr = iter(tr)
next(tr)

for movie in tr:
    imageUrl = movie.find('td',{'class': 'posterColumn'}).find("img")['src'].split("@.")[0].__str__().contents[0]
    title = movie.find('td', {'class': 'titleColumn'}).find('a').contents[0]
    year = movie.find('td', {'class': 'titleColumn'}).find('span',{'class':'secondaryInfo'}).contents[0]
    rating = movie.find('td',{'class':'ratingColumn imbdRating'}).find('storing').contents[0]
    row = title + ' - ' + year + '  ' + imageUrl + '  ' +rating
    print(row)