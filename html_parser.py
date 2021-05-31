# importing libraries
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

# global variable creation 
url = 'https://1729.com/all/'

# Parsing html into BS object
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html,'html.parser')

# Checking soup
text = soup.get_text()

# Creating first_task
def Task1():
    First_Earn = text.find('Earn',text.find('Earn',0)+5)

    Second_Earn = text.find('Earn',First_Earn)

    first_task = text[Second_Earn:text.find('read',Second_Earn)+4]

    first_task = first_task[4:].lstrip()

    return first_task





