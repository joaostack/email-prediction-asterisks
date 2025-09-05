from string import ascii_letters, digits
import m.key as KEY
import random, time, re
from colorama import Fore, Back, Style

#Contamos la ocurrencia de los asteriscos
def asteriskDetector(target):
    c = target.count("*")
    return c


char = lambda i: " ".join(random.sample(ascii_letters + digits, k=i)).upper()

def shuffle(line, name_length):
    for x in range(0, random.randint(1, 9)):
        print("\t{}".format(char(name_length)), end="\r")
        time.sleep(0.4)

    print("\t" + line)

def print_banner():

    print(f"""
{Fore.MAGENTA}
 █████╗ ███████╗████████╗███████╗██████╗ ██╗███████╗██╗  ██╗       ██╗        ██████╗ ██████╗ ███████╗██╗     ██╗██╗  ██╗
██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║██╔════╝██║ ██╔╝       ██║       ██╔═══██╗██╔══██╗██╔════╝██║     ██║╚██╗██╔╝
███████║███████╗   ██║   █████╗  ██████╔╝██║███████╗█████╔╝     ████████╗    ██║   ██║██████╔╝█████╗  ██║     ██║ ╚███╔╝ 
██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗██║╚════██║██╔═██╗     ██╔═██╔═╝    ██║   ██║██╔══██╗██╔══╝  ██║     ██║ ██╔██╗ 
██║  ██║███████║   ██║   ███████╗██║  ██║██║███████║██║  ██╗    ██████║      ╚██████╔╝██████╔╝███████╗███████╗██║██╔╝ ██╗
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝    ╚═════╝       ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  ╚═╝
Asterisk & Obelix
Fork by github.com/joaostack
Credits => github.com/QuantiKa14 (JorgeWebSec)
{Fore.RESET}""")

#Verificamos el email
def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
 
#Verificamos las API Keys
def check_APIS_KEY():
    if KEY.intelx == "":
        print(Fore.RED + "The IntelX API KEY does not exist. You will be able to use the application in a limited way." + Fore.RESET)
    else:
        print(Fore.GREEN + f"Intelx API KEY is configured correctly" + Fore.RESET)
