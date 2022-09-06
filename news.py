from bs4 import BeautifulSoup
import requests
import  re
import json

class News():
    url = "https://www.formula1.com/en/latest/all.html"
    items = {
        'elements': []
    }

    def __init__(self):
        req = requests.get(self.url)
        res = BeautifulSoup(req.text, 'html.parser')
        r1 = res.find_all(class_='f1-latest-listing--grid-item')

        for elements in r1:
            try:
                link = elements.find(class_='f1-cc').get('href')
                link="https://www.formula1.com"+link
                image_link = elements.find(class_='f1-cc--image').find(class_='f1-cc--photo').find('source').get(
                    'data-srcset').split(',')[0]
                z = elements.find(class_='f1-cc--caption')
                type = z.find('p', class_='misc--tag').get_text().split()
                title = z.find('p', class_='f1--s no-margin').get_text()
                title=re.sub('[^A-Za-z0-9]+'," ",title)

                item = {'link': link, 'image_link': image_link, 'type': type, 'title': title}
                self.items['elements'].append(item)
            except:
                pass





















