#!/usr/bin/env python
import urllib
from bs4 import BeautifulSoup
import urlparse
import requests
import os
import sys
import time
path=raw_input("Please Enter the path where you want to download your files.Skip it to remain default Path. \n")
def download_file(url):
        try:
                f = open(path+"\\"+url.split('/')[-1], 'wb')
        except:
                return
        response = requests.get(url,stream=True)
        size = int(response.headers.get('content-length'))
        CHUNK = size//100 # size for a percentage point
        if CHUNK > 1000000: # place chunk cap on >1MB files
            CHUNK = 100000 # 0.1MB
        print(size/1000000, 'mbs')
        print("Writing to file in chunks of {} bytes...".format(CHUNK))
        actual = 0 # current progress
        try:
            for chunk in response.iter_content(chunk_size=CHUNK):
                if not chunk: break
                f.write(chunk)
                actual += len(chunk) # move progress bar
                percent = int((actual/size)*100)
                if 'idlelib' in sys.modules: # you can take these conditions out if you don't have windows
                #if you do then import sys, os at the start of the program
                    if not(percent % 5):
                        ff=float(float(actual)/1000000)
                        sys.stdout.write('{}%'.format(percent)+" Downloaded="+str(ff)+"mbs"+'\r')
                        sys.stdout.flush()
                        time.sleep(1)
                else:
                    os.system('title {}% {}/{}'.format(percent, actual, size))
        except Exception as e:
            print(e)
        finally:
            f.close()
        return
url=raw_input("Please Enter The Url with http:// \n")
length1=len(url)
html=urllib.urlopen(url)
soup=BeautifulSoup(html.read(),"html.parser")
lis=[]
for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        lis.append(tag['href'])
for i in lis:
    length=len(i.split('/')[-1])
    length2=len(i)
    if(length>0 and length2>length1 and url in i):
       download_file(i)
       print (i.split('/')[-1]+" Is Downloaded") 
    else:
       print (i.split('/')[-1]+" Not Downloadable")

        
