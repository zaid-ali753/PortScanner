
#!/usr/bin/python

from socket import*
from threading import*
import optparse

def ScanConnection(trgHost,trgPort):
    try:
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((trgHost,trgPort))
        print '[+] %d / tcp Open' % trgPort
    except:
        print'[-] %d / tcp closed' % trgPort
    finally:
        sock.close()

def Scanport(trgHost,trgPorts):
    try:
        trgIP = gethostbyname(trgHost)
    except:
        print'Host %s not Found' %trgHost
    try:
        trgName = gethostbyaddr(trgIP)
        print'[+} Scanning Result for : '+ trgName[0]
    except:
        print'[+] Scanning result for : ' + trgIP
    setdefaulttimeout(1)
    for trgPort in trgPorts:
        t = Thread (target= ScanConnection , args=(trgHost,int(trgPort)))
        t.start()



def main():
    parser = optparse.OptionParser('Usage of Program' + '-H <target Host> -p <target Port>')
    parser.add_option('-H', dest = 'trgHost', type = 'string' , help = 'specify target host')
    parser.add_option('-p', dest= 'trgPort', type='string', help='specify target ports seperated by comma')
    (options,args)=parser.parse_args()
    trgHost = options.trgHost
    trgPorts = str(options.trgPort).split(',')
    if (trgHost == None) or (trgPorts[0] == None):
        print(parser.usage)
        exit(0)
    Scanport(trgHost,trgPorts)
if __name__== '__main__':
    main()
