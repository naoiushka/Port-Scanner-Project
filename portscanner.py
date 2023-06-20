# Port-Scanner-Project
# I first installed both the time and socket modules in this system for the code to work.
import time
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Target's website or IP address that needs to be scanned will be asked  
target = input('Enter website or IP address to scan: ')
# Next line will tell you that the scan has started and display the target's IP address.
target_ip = socket.gethostbyname(target)
print('Scanning target:', target_ip)
# The function for scanning ports will be shown
def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False
start = time.time()
# Following line tells the code to scan: from port 0 to 10, it should also tell you if those ports are open or closed.
# 65,535 ports can be scanned starting from 0 but for this example I will only be using 0 to 10 range.
for port in range(10):
    if port_scan(port):
     print(f'port {port} is open')
else:
    print(f'port {port} is closed')
    end = time.time()
print(f'Time taken {end - start:.2f} seconds')
