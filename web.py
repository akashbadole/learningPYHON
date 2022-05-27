import requests
from bs4 import BeautifulSoup

####                            ####
    # Only For Learning Purpose #
####                            ####


# html_url='https://www.udemy.com/topic/python/'
# html_url='https://www.coursera.org/degrees/bachelor-of-science-computer-science-london'
# html_url = 'https://bazaar.shopclues.com/mobiles-smartphones.html?facet_brand[]=Oppo&fsrc=facet_brand'
html_url = 'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi'

response = requests.get(html_url)
# print(response.status_code) #200 output
htmlcontent = response.content


soup = BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)
# print(soup.find_all('a')) # all a tag - for single find('a)
# print(soup.find_all('p')) 
# print(soup.find(id='udemy')) 
# print(soup.find_all('a')) # only url - for loop use

# for link in soup.find_all('a'):
#     print(link.get('href'))

# all images

# for image in soup.find_all('img'):
#     print(image.get('src'))

# class

# product = soup.find_all('div', class_='ud-component--topic--topic')
# print(product)

# product = soup.find_all('div', attrs={'ud-component--topic--topic'})
# print(product)


## Proper Example

titles = []
prices = []
images = []
"""
for d in soup.find_all('div', attrs={'id': 'product_list'}):
    title = d.find_all('span', attrs={'class':'prod_name'})
    # print(title.string)

    price = d.find_all('span', attrs={'class':'p_price'})
    # print(price.string)

    image = d.find_all('div', attrs={'class':'img_section'})
    # print(image)

    titles.append(title)
    prices.append(price)
    # images.append(image.get('src'))
    images.append(image)

    print(titles)
    print(prices)
    print(images)
"""

for d in soup.find_all('div', attrs={'class': '_1YokD2 _3Mn1Gg'}):
    title = d.find_all('div', attrs={'class':'_4rR01T'})
    # print(title)

    price = d.find_all('div', attrs={'class':'_30jeq3 _1_WHN1'})
    # print(price)

    image = d.find_all('img', attrs={'class':'_396cs4 _3exPp9'})
    # print(image)

    titles.append(title)
    prices.append(price)
    # images.append(image.get('src'))
    images.append(image)

    print(titles)
    print(prices)
    print(images)