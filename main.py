from subprocess import Popen, PIPE
import urllib.request
import requests
import socket
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
import json
import sys,os

def location(li):
#    response = urllib.request.urlopen("https://geolocation-db.com/json/"+str(IP[len(IP)-2]))
#    encode = response.info().get_content_charset('utf8')
#    data = json.loads(response.read().decode(encode))
    r = requests.get("http://geolocation-db.com/json/"+str(li))
    data = r.json()
    try:
        lat = float(data['latitude'])
        lon = float(data['longitude'])
        country = str(data['country_name'])
        if lat == 0.0 and log == 0.0:
            print('None')
            return(None,None,None)
        return (lat,lon,country)
    except Exception as e:
        return(None,None,None)
                
def geoloc(url):
    url1 = 'http://' + url
    url1 = urlparse(url1)
    url1 = url1.netloc
    com = Popen(['tracert', url], stdout=PIPE)
    print('IP        Country        Latitude        Longitude')
    while True:
        line = com.stdout.readline()
        line2 = str(line).replace('\\r','').replace('\\n','')
        IP = line2.split(' ')
        try:
            if '.' in IP[len(IP)-2] and IP[len(IP)-2] != url:
                lat,log,country = location(IP[len(IP)-2])
                if lat:
                    print(str(IP[len(IP)-2])+'        '+str(country)+'        '+str(lat)+'        '+str(log))
            if not line:
                break
        except Exception as e:
            print('Error')

link = sys.argv[1]
print(geoloc(str(link)))
