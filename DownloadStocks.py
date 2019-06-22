import bs4 as bs
import urllib.request
import sqlite3
import time
import threading

def run(letter):
    
    urllib.request.urlretrieve('https://www.nasdaq.com/screening/compan\
ies-by-name.aspx?letter='+letter+'&render=download', '/Users/John/Des\
ktop/StockApp/CSV_files/'+letter+'.csv')


def start():
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lst_threads = []
    
    for letter in alphabet:
        #print('Retrieving '+letter+ ' companies')
        thread = threading.Thread(target = run, args = (letter, ))
        lst_threads.append(thread)
        thread.start()
        
    for i in range(len(alphabet)):
        lst_threads[i].join()
