# importing libraries
import re
import os
# installing beautifulsoup on virtual system 
os.system('pip install --upgrade pip')
os.system('python3 -m pip install beautifulsoup4')
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

    first_task = first_task.split('   ',3)

    first_task = first_task[0].strip()

    return first_task

# Creating Second Task 
def Task2():
    First_Earn = text.find('Earn',text.find('Earn',0)+5)

    Second_Earn = text.find('Earn',First_Earn)

    Second_Task = text[text.find('read',Second_Earn)+4:text.find('read',text.find('read',Second_Earn)+4)+4].strip()

    Second_Task = Second_Task[Second_Task.find('Earn',0)+4:].strip()

    Second_Task = Second_Task.split('   ',3)

    Second_Task = Second_Task[0].strip()

    return Second_Task