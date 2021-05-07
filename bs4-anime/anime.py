from bs4 import BeautifulSoup
import requests
import csv
import json
import asyncio


file = open('2anime.json')
data = json.load(file)
#animeOne = []

def latestEpisode():
    for p in data['anime']:
        html = requests.get(p['site']).text
        oArrau = BeautifulSoup(html, "html.parser")
        output = oArrau.find("div", class_="cd-timeline-block cd-unwatched")

        for foo in output.find_all('div', class_='cd-timeline-content'):
            bar = foo.find('div', class_='cd-timeline-content-data')
            print('<h2 class="titles">' + p['title'] + '</h2>')
            print(bar)



def latestEpisodeTwo():
    for i in data['anime-two']:

        html = requests.get(i['site']).text
        oArrau = BeautifulSoup(html, "html.parser")
        output = oArrau.find("div", class_="date-text")
        print('<h2 class="titles">' + i['title'] + '</h2>')
        print(output)


latestEpisode()
latestEpisodeTwo()
 
