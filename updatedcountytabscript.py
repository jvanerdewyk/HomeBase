from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

myurl='https://en.wikipedia.org/wiki/List_of_counties_in_Iowa'

#opening up connection, grabbing the page
uClient=uReq(myurl)

page_html=uClient.read()

uClient.close()

#load html data into soup
page_soup=soup(page_html, "html.parser")

#grabs the iowa county table
table=page_soup.find("table",{"class":"wikitable sortable"})

tbody=table.find('tbody')

#county = tr.find('th')[0].text.strip()
	

for tr in tbody.findAll('tr'):
	place=tr.find('th')
	seat=tr.find('td')[1].a["title"]
	print(place, seat)
