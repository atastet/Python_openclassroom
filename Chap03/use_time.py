# -*-coding:Utf-8 -*

import time
import datetime

print(time.time())
debut = time.time()
time.sleep(1.4)
fin = time.time()
print (fin - debut)
tmps = time.localtime()
print(time.localtime().tm_mon)
ts_debut = time.mktime(tmps)
print(ts_debut)
print(time.strftime('%Y'))

date = datetime.date(2010,01,01)
print(date)
date_2 = datetime.date.fromtimestamp(debut)
print(date_2)