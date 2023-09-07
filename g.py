import urllib2

url = "https://raw.githubusercontent.com/Max7x7/solo/main/1.txt"
response = urllib2.urlopen(url)
data = response.read()

with open("1.txt", "wb") as file:
    file.write(data)

print("1.txt")
