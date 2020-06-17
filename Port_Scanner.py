import pyfiglet
import socket
import subprocess
import sys
from datetime import datetime
import time
import os
from colorama import init, Fore

init()
GREEN = Fore.GREEN
GRAY = Fore.LIGHTBLACK_EX

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

host = input("Please enter an IP address: ")

print("-" * 60)
print("Please wait, scanning remote host", host)
print("-" * 60)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)


def pscan(host, port):
    try:
        s.connect((host, port))
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except:
        return False

    else:
        return True


if os.path.exists("C:/users/humza/Desktop/python_project/Scanner_Results.txt"):
    os.remove("C:/users/humza/Desktop/python_project/Scanner_Results.txt")

xfile = open("C:/users/humza/Desktop/python_project/Scanner_Results.txt", "a+")

now = datetime.now()
dt_string = now.strftime("%y-%m-%d %H:%M:%S")
start = time.time()

command_line = (["ping -n 1"], host)
HostCheck = subprocess.Popen(command_line, stdout=subprocess.PIPE).communicate()[0]
cResult = str(HostCheck)

if cResult.find("unreachable") != -1:
    print(host, "unreachable. Aborting scan.")
    RespTup = [host, "is unreachable. Scan aborted at", dt_string, "\n"]
    RespOut = ' '.join(RespTup)
    xfile.write(RespOut)
    xfile.close()
    exit()
elif cResult.find("Received = 0") != -1:
    print(host, "not responding")
    RespTup = [host, "is not responding. Scan aborted at", dt_string, "\n"]
    RespOut = ' '.join(RespTup)
    xfile.write(RespOut)
    xfile.close()
    exit()
elif cResult.find("could not find") != -1:
    print(host, "cannot be found")
    RespTup = [host, "cannot be found. Scan aborted at", dt_string, "\n"]
    RespOut = ' '.join(RespTup)
    xfile.write(RespOut)
    xfile.close()
    exit()
elif cResult.find("Received = 1") != -1:
    print(host, 'responding. Beginning scan.')
    print("Scan beginning at: ", dt_string)
    RespTup = [host, "is responding. Beginning scan at", dt_string, "\n"]
    RespOut = ' '.join(RespTup)
    xfile.write(RespOut)
else:
    print("Unexpected error.  Try again.")
    exit()

print('Working....')

for x in range(80, 100):
    if pscan(host, x):
        print(f"{GREEN}[+]  {host}:{x} is open      ")
        CheckTup = ["Port", str(x), "is open", "\n"]
        RespOut = ' '.join(CheckTup)
        xfile.write(RespOut)
    else:
        print(f"{GRAY}[!]   {host}:{x} is closed    ", end="\r")
        CheckTup = ["Port", str(x), "is closed", "\n"]
        RespOut = ' '.join(CheckTup)
        xfile.write(RespOut)

end = time.time()
print("Task completed.")
elapsed = end - start
print("Scan completed at", dt_string)
print("Total scan time:", "%.2f" % elapsed, "seconds.")
FinTup = ["Scan completed at", str(dt_string), "\n"]
FinOut = ' '.join(FinTup)
xfile.write(FinOut)
FinTup = ["Total scan time:", "%.2f" % elapsed, "seconds.", "\n"]
FinOut = ' '.join(FinTup)
xfile.write(FinOut)
xfile.close()
