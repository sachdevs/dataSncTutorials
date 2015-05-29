import urllib2
from bs4 import BeautifulSoup

landing_page = urllib2.urlopen('http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html').read()

soup = BeautifulSoup(landing_page)
table = soup.find_all('table')
table = soup.find('tbody')
listing = []
for tr in table.find_all('tr')[1:]:
    row_content = tr.find_all('td')[2]
    link = row_content.a.get('href')
    listing.append('http://www.tdcj.state.tx.us/death_row/'+str(link))

for url in listing:
    statementPage = urllib2.urlopen(url)
    soup = BeautifulSoup(statementPage)
    p = soup.find_all('p')
    count = 0
    for text in p:
        if text.lower == "last statement":
            break
        count+=1
    for last in p[count-1:]:
        print last.contents[len(last)-1].strip().encode('utf-8').decode('ascii', 'ignore')
