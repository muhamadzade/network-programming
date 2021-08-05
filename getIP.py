import socket

def getRemoteMachineInfo(url):
    try:
        ip=socket.gethostbyname(url)
        print(f"Ip address: {url}: {ip}")
    except (socket.error,err_msg):
        print(f"{url}, {err_msg}")
    except:
        print("Invalid address")

def printMachineInfo():
    hostName=socket.gethostname()
    print(type(hostName))
    ipAddress=socket.gethostbyname(hostName)
    ipAddressServer=socket.gethostbyname(
        'DESKTOP-CTI4MIP')
    ipAddressServer=socket.gethostbyname(
        'DESKTOP-CTI4MIP')
    ipAddressClient=socket.gethostbyname(
        'U104-6')
##    print(f"hostname is {hostName}")
##    print(f"IP address is {ipAddress}")
##    print(f"IP address is {ipAddressServer}")
##    print(f"IP address is {ipAddressClient}")
    for j in range(1,5):
        for i in range(1,12):
            try:
                ipAddressClient=socket.gethostbyname(
                f'U10{j}-{i}')
                print(f"IP address is {ipAddressClient}")
            except:
                print(f"Error! U10{j}-{i}")
def findServiceName():
    for port in range(1,1025):
        try:
            s=socket.getservbyport(port,'udp')
            print(f"port: {port} name: {s}")
        except:
            pass
##            print(f"Error! {port}")
        
    
if __name__=="__main__":
    findServiceName()
##    url=input("Enter ur site address = ")
##    getRemoteMachineInfo(url)
##    printMachineInfo()
