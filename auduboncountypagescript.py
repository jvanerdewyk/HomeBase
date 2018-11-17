from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
audurl='https://en.wikipedia.org/wiki/Audubon_County,_Iowa'
uClient=uReq(audurl)
aud_html=uClient.read()
uClient.close()

aud_soup=soup(aud_html, "html.parser")
audtable=aud_soup.find("table",{"class":"infobox geography vcard"})
tbody=audtable.find('tbody')


#parses county name
head=tbody.findAll('tr')[0]
county=head.text.strip()
#parses county seat
cseat=tbody.findAll('tr')[7]
seat=cseat.text.strip()
#parses county size
csize=tbody.findAll('tr')[9]
size=csize.text.strip()
ctotal=tbody.findAll('tr')[10]
total=ctotal.text.strip()
cland=tbody.findAll('tr')[11]
land=cland.text.strip()
cwater=tbody.findAll('tr')[12]
water=cwater.text.strip()
#parses congressional district
cdis=tbody.findAll('tr')[16]
dis=cdis.text.strip()
#parses county website
cweb=tbody.findAll('tr')[18]
web=cweb.text.strip()


print(county,seat,size,total,land,water,dis,web)

