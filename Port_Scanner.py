import socket
import sys
from datetime import datetime



host = input("Please enter an IP address: ")

print ("-" * 60)
print ("Please wait, scanning remote host", host)
print ("-" * 60)

t1 = datetime.now()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)


def pscan(port):
    try:
        s.connect((host,port))
        return True
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except:
        return False


for x in range(79,85):
    if pscan(x):
        print('Port',x,'is open!!!!!')
    else:
        print('Port',x,'is closed')

t2 = datetime.now()
total =  t2 - t1
print ('Scanning Completed in: ', total)