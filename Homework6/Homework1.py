from youtube_dl import YoutubeDL
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict


#1. Open connection
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode('utf8')

#2. Find ROI 
soup = BeautifulSoup(content, "html.parser")
ul = soup.find("section","section chart-grid")
#print(ul)

# #3. Extract ROI 
li_list = ul.find_all("li")
top_list = []
number = len(li_list)
#print(li_list)
for i in range (0,number):
    li = li_list[i]
#print(li.prettify())
    title = li.h3.a.string
    artist = li.h4.a.string
    song = OrderedDict({})
    song["Title"] = title.strip()
    song["Artist"] = artist
    top_list.append(song)
    i += 1

pyexcel.save_as(records=top_list, dest_file_name="top_song_apple.xls")
a = True
while a == True:
    ask = input('Do you want download anysong? Y/N').lower()
    if ask == "y" :
        itemnumber = int(input('Download item no'))
        songdl = top_list[itemnumber-2]["Title"]
        artistdl = top_list[itemnumber-2]["Artist"]
        options = {
        'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
        'max_downloads': 1 # Tell downloader to download only the first entry (video)
        }
        dl = YoutubeDL(options)
        dl.download(['{0} {1}'.format(songdl,artistdl)])
    elif ask == "n" :
        a = False
# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1 # Tell downloader to download only the first entry (video)
# }
# dl = YoutubeDL(options)
# dl.download(['{0} {1}'.format(title,artist)])
#     post = OrderedDict({})
#     post["Title"] = title.strip()
#     post["Link"] = link
#     final_list.append(post)
#     i += 1
# #4.  Save data 
# pyexcel.save_as(records=final_list, dest_file_name="your_file.xls")