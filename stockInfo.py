

#### BROKEN ##### DO NOT USE ##########


import bs4 as bs
import urllib.request
import sqlite3


def getCompName(lst):
    iterRows = iter(lst)
    next(iterRows)

    i = 1

    for element in iterRows:
        td = element.find_all('td')
        print(str(i)+": "+td[0].text)
        i = i+1
        next(iterRows)

def getCompSymb(lst):
    iterRows = iter(lst)
    next(iterRows)

    i = 1
    for element in iterRows:
        td = element.find_all('td')
        symbol = td[1].text
        print(str(i)+": "+symbol.strip())
        i = i+1
        next(iterRows)



connection = sqlite3.connect('db/test.db')
cursor = connection.cursor()
        

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#letters = 'J'
number = str(1)



for character in letters:

    source = urllib.request.urlopen('https://www.nasdaq.com/screening/companies-by-name.aspx?letter='+str(character)+'&page=1').read()
    soup = bs.BeautifulSoup(source, 'lxml')

    pages = soup.find('a', {'id': 'two_column_main_content_lb_LastPage'})
    if(pages == None):
        pages = 1

    else:
        numPages = pages.get('href')
        pages = int(numPages.split('=',2)[2])

    

    for number in range(1, pages+1):

        print('**************PRINTING PAGE '+str(number))

        source = urllib.request.urlopen('https://www.nasdaq.com/screening/companies-by-name.aspx?letter='+str(character)+'&page='+str(number)).read()
        soup = bs.BeautifulSoup(source, 'lxml')
        
        table = soup.find('table',{'id':'CompanylistResults'})
        rowslst = table.find_all('tr')
        getCompName(rowslst)
        #getCompSymb(rowslst)
        

    
'''

symbol = 'zfgn'

source = urllib.request.urlopen('https://www.nasdaq.com/symbol/'+symbol).read()
soup = bs.BeautifulSoup(source, 'lxml')


price = soup.find('div', {'id':'qwidget_lastsale'})
symbolPrice = float(price.text[1:])

print(symbolPrice)

'''





