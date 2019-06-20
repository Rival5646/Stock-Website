import bs4 as bs
import urllib.request
import sqlite3
import time

def run():
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for letter in alphabet:

        print('Retrieving '+letter+ ' companies')
        
        urllib.request.urlretrieve('https://www.nasdaq.com/screening/compan\
ies-by-name.aspx?letter='+letter+'&render=download', '/Users/John/Des\
ktop/StockApp/CSV_files'+letter+'.csv')

