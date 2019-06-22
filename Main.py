import os
import datetime
import time
import DownloadStocks as ds
import threading
import csv
import sqlite3
import bs4 as bs
import urllib.request

import requests



def updateDB(letter):
    file = open("CSV_files/"+letter+".csv")
    csv_file = csv.reader(file)
    
    connection = sqlite3.connect('test.db', 10)
    cursor = connection.cursor()
    
    iterRow = iter(csv_file)
    next(iterRow)

    for row in iterRow:
        cursor.execute("SELECT Price FROM companiesIn"+letter+" WHERE Symbol=? ", (row[0],))
        prices = cursor.fetchall()

        if row[2] == 'n/a':
            price = None
        else:
            price = float(row[2])


        
        
        if len(prices) == 0:
            #print("Adding", row[1])
            cursor.execute(" INSERT INTO companiesIn"+letter+" VALUES(?, ?, ?, NULL, NULL)",(row[1], row[0], price))
        elif(price != prices[0][0]):
            
            #print("Updating", row[1])
            cursor.execute("UPDATE companiesIn"+letter+" SET Price=? WHERE Symbol=?", (price, row[0]))
        else:
            #print("No changes made to", row[1])
            pass
        
        
        connection.commit()

    
    file.close()
    connection.close()
    #print("Finished Updating", letter)
    




    

########################     MAIN     ##################################




letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
currentTimeStamp = str(datetime.datetime.now()).split(" ")

override = 0

if int(currentTimeStamp[1].split(":")[0]) > 16 or override:
    ds.start()





connection = sqlite3.connect('test.db')
cursor = connection.cursor()

for character in letters:

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='companiesIn"+character+"'")

    if len(cursor.fetchall()) == 1:
            pass
    else:  
        cursor.execute("Create Table companiesIn"+character+" (Company text, Symbol text, Price integer, Images text, Other text)")

connection.close()


for i in letters:
    updateDB(i)

        




    
