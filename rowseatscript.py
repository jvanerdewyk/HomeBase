from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

myurl='https://en.wikipedia.org/wiki/List_of_counties_in_Iowa'

#opening up connection, grabbing the page
uClient=uReq(myurl)

page_html=uClient.read()

uClient.close()

#html parsing
page_soup=soup(page_html, "html.parser")

#grabs the iowa county table
iacounties=page_soup.find("table",{"class":"wikitable sortable"})

#grabs each county row
counties=iacounties.findAll('tr')

#finding Adair County title, varying number(1-100) is relative to alphebetic order of iowa county.
adair=counties[1]

#finds 'th' in Adair row
adairtitle=adair.find('th')

adaircounty=adairtitle.a["title"]

#finds all 'td' in the adair row
adairtd=adair.findAll('td')

#finds title in 2nd ([1]) 'td' which is Greenfield, IA
adairseat=adairtd[1].a["title"]

print(adairseat)