import requests
from bs4 import BeautifulSoup



result = requests.get("https://bangla.bdnews24.com/")

result2 = requests.get("https://www.banglanews24.com/")

src = result.content
src2 = result2.content

soup = BeautifulSoup(src, 'lxml')
soup2 = BeautifulSoup(src2, 'lxml')

BDnews24urls = []
for h2_tag in soup.find_all('h6'):
    a_tag = h2_tag.find('a')
    BDnews24urls.append(a_tag.attrs['href'])
print("BD News 24")
print(BDnews24urls)


banglaNews24 = []
for h2_tag in soup2.find_all('h2'):
    a_tag = h2_tag.find('a')
    banglaNews24.append(a_tag.attrs['href'])
print("Bangla News 24")
print(banglaNews24)
