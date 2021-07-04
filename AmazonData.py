from bs4 import BeautifulSoup
import requests

disease = input("Enter your Query : ").replace(" ", "+")
url = 'https://google.com/search?q=amazon+' + disease
request = requests.get(url).text
soup = BeautifulSoup(request, 'lxml')

for a in soup.find_all('a', href=True):
   # print(a)
    if 'https://www.amazon.in/' in a['href']:
        page = a['href'].strip('/url?q=').split('&')
        page = page[0]
        break

print(page)
