#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys


url = "https://newyork.craigslist.org/d/jobs/search/jjj?query=cyber&sort=rel"
response = requests.get(url)
data= response.text
soup= BeautifulSoup(data,'html.parser')


#Find all the "A" tags
tags = soup.find_all('a')


# def getinfo():
#     # to grab everything
#     jobs = soup.find_all('p',{"class":"result-info"})
#     for job in jobs:
#         print("hereeee")
#         title= job.find('a',{'class':'result-title'}).text
#         date=job.find('time',{'class':'result-date'}).text
#         link = job.find('a',{'class':'result-title'}).get('href')
#         #in case its missing
#         addressTag= job.find('span',{'class':'result-hood'})
#         address= addressTag.text[2:-1] if addressTag else print("N/A")

#         print(f'Job Title: {title} \nLocation  {address}, \nDate {date} \nLink {link} \n--------')



def getlinks():
    #GET ALL THE LINKS 
    for tag in tags:
        print(tag.get('href'))

def title():
    #finding all titles for Job searches (look at a tags to modify the titles variable)
    titles= soup.find_all("a", {"class":"result-title"})
    for title in titles:
        print(title.text)


def where():
    #find all addresses
    addresses= soup.find_all("span", {"class": "result-hood"})
    for address in addresses:
        print(address.text)


def looking(look4):
    if look4 ==1:
        print("her")
        getlinks()
    elif look4==2:
        title()
    elif look4 ==3:
        where()
    else:
        getinfo()


print("what are you looking for? 1,,2,3,4")
x= input()
looking(x)



#######################TEST ENVORIMENT START#######################################################3
def getinfo():
    # to grab everything
    jobs = soup.find_all('p',{"class":"result-info"})
    for job in jobs:
        print("hereeee")
        title= job.find('a',{'class':'result-title'}).text
        date=job.find('time',{'class':'result-date'}).text
        link = job.find('a',{'class':'result-title'}).get('href')
        #in case its missing
        addressTag= job.find('span',{'class':'result-hood'})
        address= addressTag.text[2:-1] if addressTag else print("N/A")

        print(f'Job Title: {title} \nLocation  {address}, \nDate {date} \nLink {link} \n--------')

#######################TEST ENVORIMNET END##########################################################3