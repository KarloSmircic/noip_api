# noip_api
A little noip ddns api for python.


### Requirements 
* socket
* requests
* cryptography

### Description
* `login` function logs you in with your username and password
* `saveLoginInfo` function save your username and password encrypted in noip.config file
* `loadLoginInfo` function loads your username and password from noip.config file
* `getCurrent` function returns current ip saved in your hostname
* `setDNS` function sets given ip to your hostname
* `getMyIP` function returns your current public ip address

### Example 1
```py
import noip_api

username = ""
password = ""
hostname = ""

DDNS = noip_api.noip(hostname)
DDNS.login(username=username, password=password)
print(DDNS.getMyIP())
print(DDNS.getCurrent())
DDNS.setDNS(ip=DDNS.getMyIP())
```
### Example 2
```py
import noip_api

username = ""
password = ""
hostname = ""

DDNS = noip_api.noip(hostname)
DDNS.saveLoginInfo(username=username, password=password)
```
### Example 3
```py
import noip_api

username = ""
password = ""
hostname = ""

DDNS = noip_api.noip(hostname)
DDNS.loadLoginInfo()
DDNS.setDNS(ip=DDNS.getMyIP())
```
