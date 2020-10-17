import socket
import requests
from cryptography.fernet import Fernet
from bs4 import BeautifulSoup

class noip:
    def __init__(self, hostname):
        self.hostname = hostname

    def login(self, username, password):
        self.username = username
        self.password = password

    def saveLoginInfo(self, username, password):
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encoded_username = cipher_suite.encrypt(bytes(username, "utf-8"))
        encoded_password = cipher_suite.encrypt(bytes(password, "utf-8"))
        with open("noip.config", "w") as f:
            f.write(str(key)[2:-1]+"\n"+str(encoded_username)[2:-1]+"\n"+str(encoded_password)[2:-1])

    def loadLoginInfo(self):
        with open("noip.config", "r") as f:
            file = f.read()
            file = file.split("\n")
            key = file[0]
            username = file[1]
            password = file[2]
            cipher_suite = Fernet(key)
            decoded_username = str(cipher_suite.decrypt(bytes(username, "utf-8")))[2:-1]
            decoded_password = str(cipher_suite.decrypt(bytes(password, "utf-8")))[2:-1]
            self.username = decoded_username
            self.password = decoded_password

    def getCurrent(self):
        hostnameIp = socket.gethostbyname(self.hostname)
        return hostnameIp

    def setDNS(self, ip):
        r = requests.get("http://{}:{}@dynupdate.no-ip.com/nic/update?hostname={}&myip={}".format(self.username, self.password, self.hostname, ip))

    def getMyIP(self):
        ip = requests.get("http://api.ipify.org").text
        return ip

    def testOpenPort(self, host, port):
        url = "https://www.ipfingerprints.com/scripts/getPortsInfo.php"
        data = {"remoteHost":str(host), "start_port":str(port), "end_port":str(port),"normalScan":"Yes", "scan_type":"connect", "ping_type":"none"}
        req = requests.post(url, data=data)
        soup = BeautifulSoup(req.text.replace("\\n", "").replace("\\", ""), features="html.parser")
        spans = soup.findAll("span", attrs={'class':'pass'})
        if len(spans) >0:
            return spans[0].text
        else:
            spans = soup.findAll("span", attrs={'class':'fail'})
            return spans[0].text

