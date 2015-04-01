#GODADDY DOMAIN ANALYZER
#AUTHOR VISHNUVARDHAN MURUGHIAN


#!/usr/bin/env python3
from ftplib import FTP
import pprint
ftp = FTP('ftp.godaddy.com')
print("Welcome:", ftp.getwelcome())
ftp.login("auctions","")
print("Current working directory:", ftp.pwd())
print ("FILES:")
pprint.pprint (ftp.dir("/"))

try:
	#local_filename = os.path.join(r"c:\myfolder", filename)
    #lf = open(local_filename, "wb")
    with open ('end_today_feed.xml.zip' , 'wb') as f:
    	print (ftp.retrbinary('RETR end_today_feed.xml.zip' , f.write))
    #lf.close()
    #ftp.retrbinary("RETR " + end_today_feed.xml.zip ,open(i, 'wb').write)
except:
    print ("Error")

#ftp.quit()


