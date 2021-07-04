message = input("Enter your Query : ").replace(" ","+")
url = 'https://google.com/search?q=video+on+' + message[4:]
request = requests.get(url).text
soup = BeautifulSoup(request, 'lxml')
for a in soup.find_all('a', href=True):
    if 'https://www.youtube.com/' in a['href']:
        page=a['href'].strip('/url?q=').split('&')
        page=page[0]
        print(page)
        break;
