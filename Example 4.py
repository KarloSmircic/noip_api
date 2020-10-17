import noip_api

hostname = ""
port = ""

DDNS = noip_api.noip(hostname)
print(DDNS.testOpenPort(DDNS.getMyIP(), port))
