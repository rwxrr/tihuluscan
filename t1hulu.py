#!/usr/bin/env python 

# python sürümünüze dikkat etmeniz gerekmektedir, eğer default olarak python3 sürümünü kullanıyorsanız raw_input fonksiyonu calismayacaktir.

import socket,subprocess,sys
from datetime import datetime


#ekranı temizleme 
subprocess.call('clear',shell=True)

remoteServer=raw_input("Taranacak Host'u Giriniz:")
remoteServerIP=socket.gethostbyname(remoteServer) 

print ("-" * 80)
print ("Lütfen Bekleyiniz, taranıyor....",remoteServerIP)
print ("-" * 80)

timeStart=datetime.now()


# Şimdi 1-1024 arası portları tarayacağız. 

try:
	for port in range(1,1025):
		
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		# Baglanti cesidini belirtiyoruz, TCP ? UDP ?
		result=sock.connect_ex((remoteServerIP,port))
		# Belirtilen host ip adresini 1-1024 port arası taranacak
		if result==0:
			print ("Open Port : ", port)
		sock.close()

except KeyboardInterrupt:
	print ("Çıkmak için CTRL + C")
	sys.exit()

except socket.gaierror:
	print ("Hostname not found, exiting")
	sys.exit()
except socket.error:
	print ("Couldn't connect to server")
	sys.exit()


# geçen süreyi tekrar hesaplayalim.

timeFinish=datetime.now()

totalTime=timeFinish-timeStart

print ('Tarama Süresi : ',totalTime)