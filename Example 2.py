import noip_api

username = ""
password = ""
hostname = ""

DDNS = noip_api.noip(hostname)
DDNS.saveLoginInfo(username=username, password=password)
