import requests
from bs4 import BeautifulSoup

url = input("Enter the URL: ")
finalUrl = ""


if "www." in url:
    finalUrl = url.replace("www.", "http://")
else:
    finalUrl = "https://" + url

print("url : " + finalUrl)


# get web page html content
r = requests.get(finalUrl)

# grab all the text and parse to html
soup = BeautifulSoup(r.text, 'html.parser')

formatted_link = []

print(soup.title)

for link in soup.find_all('a'):
    print("URL 'a'  : " + link.get('href'))
