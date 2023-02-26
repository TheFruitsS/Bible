import requests
from bs4 import BeautifulSoup


"""finding from bible Chapters"""

res = requests.get('https://www.bible.com/bible/1713/GEN.1.CSB')

soup = BeautifulSoup(res.text, 'html.parser')
raw_content = soup.find_all('div').__str__()
bible_chapter = soup.find_all('div', class_='yv-bible-text').__str__()


#file in html with Bible Chapter
f = open('index1.html', 'w')
f.write(raw_content)
f.close()
f = open('index1.html', 'r')

#file in html with Bible Chapter
f1 = open('index2.html', 'w')
f1.write(bible_chapter)
f1.close()
f1 = open('index2.html', 'r')
