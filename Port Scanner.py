# 1. Create Python Port Scanner to find open port in 1 to 1025 range
# 2. Calculate time to find open ports; display start and end time on screen and save into file
# 3. Save open ports and nay errors into file
import socket
from pyfiglet import Figlet
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)

host = input("Please enter the IP you want to scan ")
port = int(input("Please enter the port you want to scan: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")


portScanner(port)