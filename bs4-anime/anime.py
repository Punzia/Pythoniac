from bs4 import BeautifulSoup
import requests
import json

file = open('2anime.json')
data = json.load(file)

def latestEpisode():
    for p in data['anime']:
        html = requests.get(p['site']).text
        oArrau = BeautifulSoup(html, "html.parser")
        #check if the inactive tags are available.
        if oArrau.find_all("div", {"class": "cd-timeline-block cd-inactive"}):           
             output = oArrau.find("div", class_="cd-timeline-block cd-inactive")
             #check the latest first element the current coming episode (If the date is next week, the episode is out!) 
             for foo in output.find_all('div', class_='cd-timeline-content'):
                 bar = foo.find('div', class_='cd-timeline-content-data')
                 print('<h2 class="titles">' + p['title'] + '</h2>')
                 print(bar)
        #print('<h2 class="titles">' + p['title'] + '</h2>')

def latestEpisodeTwo():
    for i in data['anime-two']:

        html = requests.get(i['site']).text
        oArrau = BeautifulSoup(html, "html.parser")
        output = oArrau.find("div", class_="date-text")
        print('<h2 class="titles">' + i['title'] + '</h2>')
        print(output)


latestEpisode()
latestEpisodeTwo()

