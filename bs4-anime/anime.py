from bs4 import BeautifulSoup
import requests
import json


file = open('anime.json')
data = json.load(file)
for p in data['anime']:
    
    html = requests.get(p['site']).text
    oArrau = BeautifulSoup(html, "html.parser")
    output = oArrau.find("div", class_="cd-timeline-block cd-inactive")
    #print('Website: ' + p['site'])
    print('<h2 style="color: white; text-align:center;">' + p['title'] + '</h2>')
    print(output)

youcdn = [
    # Your countdown seems to have more accurate release, otherwise Episodate is currently under DMCA
    "https://yourcountdown.to/attack-on-titan"
    # Still in an array in case adding more links
]
#for x in epdate:
#    html = requests.get(x).text
#    oArrau = BeautifulSoup(html, "html.parser")
#    output = oArrau.find_all("div", class_="cd-timeline-block cd-inactive")
#    print(output)
# Just uncommented due to using external .json file instead.

for y in youcdn:
    html = requests.get(y).text
    oArrau = BeautifulSoup(html, "html.parser")
    output = oArrau.find_all("div", class_="date-text")
    print(output)
