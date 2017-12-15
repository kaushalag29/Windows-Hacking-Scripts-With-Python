#!/usr/bin/env python
import shutil
import getpass
user=getpass.getuser()
shutil.copy2("name-of-file-to-copy.pyw", "C:\Users\\"+user+"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")

