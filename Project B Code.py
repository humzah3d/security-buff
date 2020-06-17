
# Import required modules
import socket
import subprocess
from datetime import datetime, time
import time
import os

# Create a function to use the connect command for a given host and port
def CheckPort(host, port):
    s=socket.socket()
    try:
        s.connect((host,port))
    except:
        return False
    else:
        return True

# Every scan should create a new file.  Check if file exists.  If so, delete it
if os.path.exists("C:/users/JediB/Documents/PythonFiles/PortScanResults.txt"):
    os.remove("C:/users/JediB/Documents/PythonFiles/PortScanResults.txt")
# open file in append+read mode, create if not exist
xfile = open("C:/users/JediB/Documents/PythonFiles/PortScanResults.txt", "a+")

# Seek user input and validate format using try block
host = input("Enter host IP address: ")
MinRange = int(input('Enter starting port number: '))
MaxRange = int(input('Enter ending port number: '))
CheckRange = range(MinRange, MaxRange+1, 1)

#Get current time
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
start = time.time()

#verify that host is alive before proceeding and notify user of result
command_line = (["ping -n 1 "], host)
HostCheck = subprocess.Popen(command_line,stdout=subprocess.PIPE).communicate()[0]
cResult = str(HostCheck)
#print(cResult)
if (cResult.find("unreachable") != -1):
    print(host, " unreachable. Aborting scan.")
    RespTup = [host, "is unreachable. Scan aborted at", dt_string, "\n"]  # create the tuple of valued to be written to file
    RespOut = ' '.join(RespTup)  # use join function to create a string for the write command
    xfile.write(RespOut)
    xfile.close()
    exit()
elif (cResult.find("Received = 0") != -1):
    print(host, "not responding")
    RespTup = [host, "is not responding. Scan aborted at", dt_string, "\n"]  # create the tuple of valued to be written to file
    RespOut = ' '.join(RespTup)  # use join function to create a string for the write command
    xfile.write(RespOut)
    xfile.close()
    exit()
elif (cResult.find("could not find") != -1):
    print(host, "cannot be found")
    RespTup = [host, "cannot be found. Scan aborted at", dt_string, "\n"]  # create the tuple of valued to be written to file
    RespOut = ' '.join(RespTup)  # use join function to create a string for the write command
    xfile.write(RespOut)
    xfile.close()
    exit()
elif (cResult.find("Received = 1") != -1):
    print(host, 'responding. Beginning scan.')
    print("Scan beginning at: ", dt_string)
    RespTup = [host, "is responding. Beginning scan at", dt_string, "\n"]
    RespOut = ' '.join(RespTup)
    xfile.write(RespOut)
else:
    print("Unexpected error.  Try again.")
    exit()

#Notify user process has started
print('Working.....')

#check each port in the range
for x in CheckRange:
    if CheckPort(host,x):
        print("port ", x, " is open")
        CheckTup = ["Port", str(x), "is open.", "\n"]
        RespOut = ' '.join(CheckTup)
        xfile.write(RespOut)

    else:
        print('port ', x, ' is closed')
        CheckTup = ["Port", str(x), "is closed.", "\n"]
        RespOut = ' '.join(CheckTup)
        xfile.write(RespOut)

#Notify user process has finished
end = time.time()
print("Task completed. Port range", MinRange, " - ", MaxRange, " has been scanned.")
elapsed = end - start
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("Scan completed at: ", dt_string)
print("Total scan time: ", "%.2f" % elapsed, "seconds.")
FinTup = ["Scan completed at", str(dt_string), "\n"]
FinOut = ' '.join(FinTup)
xfile.write(FinOut)
FinTup = ["Total scan time:","%.2f" % elapsed, "seconds.", "\n"]
FinOut = ' '.join(FinTup)
xfile.write(FinOut)
xfile.close()
