import os
import sys
import time
from os import system
from time import sleep

#This script is Redeveloped by Zero || ColdBreazy.
#This is created for educational purposes only.

try:
    import requests
except ImportError:
    os.system('apt-get install python3')
    os.system('pip3 install requests')

try:
	request = requests.get("https://www.google.com/search?q=freemailsender.com", timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("[!] Oops, It looks like you have no Internet [!]")
    sys.exit()

import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'


import requests

# my website url
php_url = "https://paladinpal.000webhostapp.com/gapi.php"

# default value for views
views = None

# Sending a GET request to my PHP script
response = requests.get(php_url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    views = data.get("views")  # Access the "views" field

# Print the number of views outside of the if statement
if views is not None:
    print(f"Get : {views}")
else:
    print("Unable to fetch repository views.")

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

logo = """

\033[1;35m
    ░██████╗██████╗░░█████╗░░█████╗░███████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
    ╚█████╗░██████╔╝██║░░██║██║░░██║█████╗░░
    ░╚═══██╗██╔═══╝░██║░░██║██║░░██║██╔══╝░░
    ██████╔╝██║░░░░░╚█████╔╝╚█████╔╝██║░░░░░
    ╚═════╝░╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░░░░

      \033[1;31m
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      \033[1;32m [\033[1;33m+\033[1;32m]\033[1;36m REMASTERED BY \033[1;31m(\033[1;33mZ3R0\033[1;31m)~~~~~~~|
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      \033[1;32m [\033[1;33m+\033[1;32m]\033[1;36m FACEBOOK \033[1;31m     (\033[1;33mZ3RO\033[1;31m)~~~~~~~|
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
system("clear")
print (logo)
hprint(G + '   [+] ADVANCE PHISHING REMASTERED')
hprint(f'   [+] TOTAL VIEWS TODAY : {views}')
sleep(2)
print()
name = input(R + "   [+] Enter Sender's Name" + Y + " => " + G)
print("")

sender = input(R + "   [+] Enter Sender's Email" + Y + " => " + G)
print("")

receiver = input(R + "   [+] Enter Victim  Email" + Y + " => " + G)
print("")

subject = input(R + "   [+] Enter Subject" + Y + " => " + G)
print("")

body = input(R + "   [+] Enter the Message" + Y + " => " + G)
print("")

files = {
    'name': (None, name),
    'subject': (None, subject),
    'to': (None, receiver),
    'email': (None, sender),
    'message': (None, body),
    'send': (None, "send"),
}

response = requests.post('https://paladinpal.000webhostapp.com/Test/phpEmail/mail.php', files=files)

hprint(R + ' Sending email to ' + C + ':' + receiver + ' ...')
time.sleep(3)
print(response)
time.sleep(4)

print("[!] an error occured or Yoy Have modified the code")
