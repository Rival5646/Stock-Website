

import sqlite3
import bs4 as bs
import urllib.request



letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for character in letters:

    connection = sqlite3.connect("Databases/"+character+'.db')
    cursor = connection.cursor()

    connection2 = sqlite3.connect('test.db')
    cursor2 = connection2.cursor()

    cursor2.execute("SELECT Symbol FROM companiesIn" + character+" WHERE ROWID > 0")

    companies = cursor2.fetchall()

    connection2.close()





    for comp in companies:

        c = comp[0].strip()
        print(c)


        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+c+"'")

        ci = cursor.fetchall()

        if len(ci) == 1:
            pass
        else:

            cursor.execute("Create Table '"+c+"' (Month integer, Day integer, Year integer, Price integer)")
            connection.commit()


        try:
            source = urllib.request.urlopen('https://www.nasdaq.com/symbol/'+c+'/historical').read()
        except:
            source = urllib.request.urlopen('https://www.nasdaq.com/symbol/' + c.lower() + '/historical').read()


        soup = bs.BeautifulSoup(source, 'lxml')

        download = soup.find("div", {"id":"quotes_content_left_pnlAJAX"})

        for i in download.find_all("tr")[2:]:
            date = i.find_all("td")[0].text.strip()
            price = i.find_all("td")[4].text.strip()

            splitDate = date.split("/")






            cursor.execute("SELECT Month, Day, Year FROM '" + c + "' WHERE \
            Month=? AND Day=? AND Year=? ", (int(splitDate[0]), int(splitDate[1]), int(splitDate[2])))

            info = cursor.fetchall()

            if len(info) == 0:
                print("Adding "+ date +" to "+ c)

                cursor.execute(" INSERT INTO '" + c + "' VALUES(?, ?, ?, ?)",(int(splitDate[0]), int(splitDate[1]),\
                                                                                int(splitDate[2]), float(price)))
                connection.commit()
            else:
                pass
    print("Finished loading history for", character)

