import sys
import json
import string
from pprint import pprint
import re
from json.decoder import JSONDecoder
import os
import requests


data = '{"username":"admin","password":"SENHA","strict":true}'
response = requests.post('https://200.0.9.2:8443/api/login', data=data, verify=False)
cookies = {
}
response = requests.get('https://200.0.9.2:8443/api/s/default/stat/device', cookies=cookies, verify=False)


print ("<body>")
with open('output.json') as json_file2:
        datas = json.load(json_file2)
        x = 0
        while(True):
                try:
                        print ('<font style="color:#525244;">')
                        print ("\n"+json.dumps(datas["data"][x]["name"]))
                        #print (json.dumps(datas["data"][x]["vap_table"][0]["essid"])+ " " + json.dumps(datas["data"][x]["adopted"]) )
                        a= (json.dumps(datas["data"][x]["adopted"]))
                        if(a) == "true":     #VERFIFICACAO
                                a = ("OK")
                                b =(json.dumps(datas["data"][x]["vap_table"][0]["essid"]))
                                #print (json.dumps(datas["data"][x]["vap_table"][0]["essid"])+ " "+a)
                                print ('<font color="#673ab7">'+b+'</font></font><font color=green><b>'+a+'</b></font></font><br>')
                        x += 1
                except:
                        print("</body>")
                        break
