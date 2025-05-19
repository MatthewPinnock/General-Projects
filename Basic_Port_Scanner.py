# Importing necessary modules
import socket  # For network connections and communication
import pyfiglet  # For creating ASCII art banners

# Generate and display an ASCII banner for "PORT SCANNER"
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Create a TCP socket using IPv4 addressing
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)  # Set a timeout of 1 second for socket connections

# Prompt user for IP address and port number to scan
host = input("Please enter the IP you want to scan ")
port = int(input("Please enter the port you want to scan: "))

# Define a function to scan a given port
def portScanner(port):
    # Check if the port is open or closed
    if s.connect_ex((host, port)):  # Returns 0 if the connection is successful
        print("The port is closed")
    else:
        print("The port is open")

# Call the portScanner function with the specified port
portScanner(port)
