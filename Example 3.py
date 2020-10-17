import noip_api

hostname = ""

DDNS = noip_api.noip(hostname)
DDNS.loadLoginInfo()
DDNS.setDNS(ip=DDNS.getMyIP())