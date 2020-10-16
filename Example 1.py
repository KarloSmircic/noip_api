import noip_api

username = ""
password = ""
hostname = ""

DDNS = noip_api.noip(hostname)
DDNS.login(username=username, password=password)
print(DDNS.getMyIP())
print(DDNS.getCurrent())
DDNS.setDNS(ip=DDNS.getMyIP())