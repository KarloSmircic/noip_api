import noip_api

username = ""
password = ""
hostname = ""

DDNS = noip_api.noip(hostname)
DDNS.loadLoginInfo()
DDNS.setDNS(ip=DDNS.getMyIP())