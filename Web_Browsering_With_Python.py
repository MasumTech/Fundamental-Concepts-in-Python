'''
import builtins
print(dir(builtins))
             
import math
print(math.pi)
print(math.pow(2,3))
print(math.pow(3,2))
print(math.sqrt(25))
print(math.floor(5.3))
print(math.ceil(5.3))            
       
import datetime
today = datetime.datetime.today()
print(today)
 
 
from datetime import datetime
d = datetime.today()
print(d)

'''
 

import webbrowser
url = "http://fb.com"
webbrowser.open(url)


import webbrowser as wb
url = "http://linkedin.com"
wb.open(url)
