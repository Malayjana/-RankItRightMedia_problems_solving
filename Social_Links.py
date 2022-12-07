import requests
import re
from bs4 import BeautifulSoup
url = input('Enter the URL: ')

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
find = soup.find_all('a')
lst=[]
Contact=[]
Social_links=[]
Email=[]
re_email='([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
re_phone= '^tel:(\+?\d{0,2}\-?\s?)?\(?\d{3,4}\)?[\s.-]?\d{3}[\s.-]?\d{3,4}$'
for i in find:
  lst.append(i['href'])

for elem in lst:
  if re.search(re_phone, elem):
    Contact.append(elem)
  if elem.startswith('https://www.facebook') or elem.startswith('https://www.linkedin'):
    Social_links.append(elem)
  if re.search(re_email,elem):
    Email.append(elem)

print('Social Links-',end='\n')
for elem in Social_links:
  print(elem)
print('Email/s-',end='\n')
for elem in Email:
  print(elem)
print('Contact:',end='\n')
for elem in Contact:
  print(elem)
