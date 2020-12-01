#imports aqui meu bem
import requests
import os
import sys
import argparse
import platform
from time import sleep
from crayons import *
from faker import Faker
# fim dos imports.

#cores.
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"
tPreto = "\033[1;30m"
fVermelho = "\033[1;31m"
tVerde = "\033[1;32m"
tAmarelo = "\033[1;33m"
tAzul = "\033[1;34m"
tMagenta = "\033[1;35m"
tCiano = "\033[1;36m"
tCinzaClaro = "\033[1;37m"
tCinzaEscuro = "\033[1;90m"
tVermelhoClaro = "\033[1;91m"
tVerdeClaro  = "\033[1;92m"
tAmareloClaro = "\033[1;93m"
tAzulClaro = "\033[1;94m"
tMagentaClaro = "\033[1;95m"
tCianoClaro = "\033[1;96m"
tBranco = "\033[1;97m"
tNegrito = "\033[;1m"
tInverte = "\033[;7m"
tReset = "\033[0;0m"
# fim das cores.
parser = argparse.ArgumentParser()
fake = Faker()
parser.add_argument('url', help='URL no qual você deseja brutar;')
parser.add_argument('-w', '--wordlist')
parser.add_argument('-t', '--timeout')
args = parser.parse_args()
print(args.timeout)
if 'http' not in args.url:
    args.url = 'https://{}'.format(args.url)

if args.url[len(args.url)-1:] != '/':
    args.url += '/'
words = []
os.system(['clear', 'cls'][os.name == 'nt'])
print(white + """Dá uma força no meu github! :)
https://github.com/march0s1as""")
sleep(2)
os.system(['clear', 'cls'][os.name == 'nt'])
sleep(2)
print(fVermelho + """
         .AMMMMMMMMMMA.          
       .AV. :::.:.:.::MA.        
      A' :..        : .:`A       
     A'..              . `A.     https://discord.gg/v5d3PZ9
    A' :.    :::::::::  : :`A           
    M  .    :::.:.:.:::  . .M             by: march0s1as.
    M  :   ::.:.....::.:   .M                       
    V : :.::.:........:.:  :V    
   A  A:    ..:...:...:.   A A   
  .V  MA:.....:M.::.::. .:AM.M   
 A'  .VMMMMMMMMM:.:AMMMMMMMV: A  
:M .  .`VMMMMMMV.:A `VMMMMV .:M: 
 V.:.  ..`VMMMV.:AM..`VMV' .: V  
  V.  .:. .....:AMMA. . .:. .V   
   VMM...: ...:.MMMM.: .: MMV    
       `VM: . ..M.:M..:::M'      
         `M::. .:.... .::M       
          M:.  :. .... ..M       
 VK       V:  M:. M. :M .V       
          `V.:M.. M. :M.V' 
""")
sleep(2)
print(white + "Paciência.. estamos varrendo os diretórios do site.")
sleep(2)
print(tCiano + "..aceita um café?")
print(" ")
sleep(4)
def timeout():
    if args.timeout != None:
        time.sleep(int(args.timeout))
f = open(args.wordlist)
for each in f:
    words.append(each.replace('\n', ''))
f.close()
times = 0
while times != len(words):
    try:
        req = requests.get(args.url + '{}'.format(words[times]),
                        headers={'User-Agent':fake.user_agent(),
                            'content-type':'text'
                        }
        )
        if req.status_code == 200:
            print(tVerde + ('{} --> este diretório existe. (CODE: 200)'.format(args.url + '{}'.format(words[times]))))
        times += 1
        if req.status_code == 403:
            print(tAmarelo + ('{} --> sem permissão. (CODE: 403)'.format(args.url + '{}'.format(words[times]))))
        timeout()
    except KeyboardInterrupt:
        break
