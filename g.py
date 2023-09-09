import urllib2

url = "https://www.vpnbook.com/free-openvpn-account/vpnbook-openvpn-pl226.zip"
response = urllib2.urlopen(url)
data = response.read()

with open("1.txt", "wb") as file:
    file.write(data)

print("1.txt")


