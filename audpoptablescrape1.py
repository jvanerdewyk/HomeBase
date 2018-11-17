from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
audurl='https://en.wikipedia.org/wiki/Audubon_County,_Iowa'
uClient=uReq(audurl)
aud_html=uClient.read()
uClient.close()

aud_soup=soup(aud_html, "html.parser")
audpoptable=aud_soup.find("table",{"class":"toccolours"})
popbody=audpoptable.find('tbody')

#parsing title and decennial populations
#ptitle=popbody.findAll('tr')[0]
#poptitle=ptitle.text.strip()
#pheads=popbody.findAll('tr')[1]
#popheads=pheads.text.strip()

for tr in popbody.findAll('tr'):
    year=tr.findAll('td')[0]
    print(year)