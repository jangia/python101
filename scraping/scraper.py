from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import re

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response)
csv_file = open("email_list.csv", "w")

print soup.html.head.title.string
for link in soup.findAll("a"):
    if link.string == 'See full profile':
        person_details_url = url[0:-1] + link['href']
        person_html = urlopen(person_details_url).read()
        person_soup = BeautifulSoup(person_html)
        # find email
        email = person_soup.find("span", attrs={"class": "email"}).string
        name = ''
        name_el = person_soup.findAll('h1')
        # find name
        for el in name_el:
            if el.string != 'Hello, ninja!':
                name = el.string

        # find city
        city = person_soup.find('span', attrs={'data-city': True}).string
        #city = person_soup.find('span', attrs={'data-city': re.compile("[A-Z][a-z]+")}).string
        print name, email, city
        person_string = '{name},{email},{city}\n'.format(name=name, email=email, city=city)
        csv_file.write(person_string)
        # print person_soup
# print soup.html.body.div.div.h1.string
csv_file.close()
