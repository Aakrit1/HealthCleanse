from bs4 import BeautifulSoup
import requests
import json


disease = input("Enter your Disease : ").replace(" ", "+")
url = 'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&order=relevance&q=natural+remedies+for+{}&type=video&key=AIzaSyCEraPha5VpVfVDAwd7LIJ274PYXTyBEr0'.format(
    disease)
request = requests.get(url).text
soup = BeautifulSoup(request, 'lxml')
video = json.loads(soup.p.text)
video_id = video["items"][0]["id"]["videoId"]

link = 'https://www.youtube.com/watch?v='+video_id
print(link)
