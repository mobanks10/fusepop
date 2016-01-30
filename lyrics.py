__author__ = 'Sumanth Srinivasan'


from lxml import html
import requests
from titlecase import titlecase
import fileinput

textFile = open("text.txt", "a")

page = requests.get('http://www.billboard.com/charts/year-end/2015/hot-100-songs')
tree = html.fromstring(page.content)

title = tree.xpath('//h2[@class="chart-row__song"]/text()')
artist = tree.xpath('//a[@class="chart-row__link"]/text()')

print('parse Step1')
for i in range(100):

    title[i] = title[i].strip()
    title[i] = title[i].lower()
    artist[i] = artist[i].strip()
    artist[i] = artist[i].lower()

# if artist[i].find('&', beg=0, end=len(artist[i])):
    try:
        truncPosition = artist[i].index('&')
        # artist[i] = titlecase(artist[i].lower())
        artist[i] = artist[i][:truncPosition-2]
        artist[i] = artist[i].strip()
        # print(title[i], '-', artist[i])
        # print(truncPosition)
    except ValueError:
        continue

print('parse Step2')
for i in range(100):
    title[i] = title[i].strip()

    # title[i] = titlecase(title[i].lower())
    artist[i] = artist[i].strip()

    # if artist[i].find('&', beg=0, end=len(artist[i])):
    try:
        truncPosition = artist[i].index('Featuring')
        artist[i] = titlecase(artist[i].lower())
        artist[i] = artist[i][:truncPosition-1]
        artist[i] = artist[i].strip()
        # print(title[i], '-', artist[i])
        # print(truncPosition)
    except ValueError:
        continue

count = 0
for i in range(100):
    artist[i] = artist[i].split()
    title[i] = title[i].split()
    artist[i] = "-".join(artist[i])
    title[i] = "-".join(title[i])
    urlTag = title[i]+'-lyrics-'+artist[i]

    urlFull = 'http://www.metrolyrics.com/'+urlTag+'.html'
    print(urlFull)

    page2 = requests.get(urlFull)
    tree2 = html.fromstring(page2.content)
    lyrics = tree2.xpath('//p[@class="verse"]/text()')
    print(lyrics)
    textFile.writelines(["%s\n" % item  for item in lyrics])
    count += 1


textFile.close()

with open('text.txt','r+') as file:
    for line in file:
        if line.strip():
            file.write(line)


# print(count)
# print('out of 100')
#
#
#
# page2 = requests.get('http://www.metrolyrics.com/dont-lyrics-ed-sheeran.html')
# tree2 = html.fromstring(page2.content)
# lyrics = tree2.xpath('//p[@class="verse"]/text()')
# print(lyrics)
# textFile = open("text.txt", "a")
# textFile.writelines(["%s\n" % item  for item in lyrics])
# #api.azapi.generating('Radiohead','Reckoner', True)