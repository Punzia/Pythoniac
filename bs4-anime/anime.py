from bs4 import BeautifulSoup
import requests
import csv
import json
import asyncio

# https://horsetourneys.com/leaderboard/contest/900537/quick-early-bird-500-guaranteed-w-no-limit-p-p.html
# https://erikrood.com/Python_References/web_scrape.html
# data-datetime="2020-10-23T16:25:00+00:00"
# https://www.episodate.com/tv-show/majo-no-tabitabi

file = open('2anime.json')
data = json.load(file)
#animeOne = []

def latestEpisode():
    for p in data['anime']:
        html = requests.get(p['site']).text
        oArrau = BeautifulSoup(html, "html.parser")
        output = oArrau.find("div", class_="cd-timeline-block cd-inactive")

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
 
