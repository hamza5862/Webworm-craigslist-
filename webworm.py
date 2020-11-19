#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys
import pandas as pd

print(" Please Name the job are you looking for!")
enter=input()
x = enter.replace(" ", "+") 


# url = "https://newyork.craigslist.org/d/jobs/search/jjj?query=cyber&sort=rel"
url = f"https://newyork.craigslist.org/search/jjj?query={x}&sort=rel"
print(url)
response = requests.get(url)
data= response.text
soup= BeautifulSoup(data,'html.parser')


#Find all the "A" tags
tags = soup.find_all('a')




def getlinks():
    #GET ALL THE LINKS 
    for tag in tags:
        print(tag.get('href'))
# getlinks()
def title():
    #finding all titles for Job searches (look at a tags to modify the titles variable)
    titles= soup.find_all("a", {"class":"result-title"})
    for title in titles:
        print(title.text)
# title()

def where():
    #find all addresses
    addresses= soup.find_all("span", {"class": "result-hood"})
    for address in addresses:
        print(address.text)
    
# where()



#######################Getting jobs >START< #######################################################3



def getinfo():
#     # to grab everything
    jobs = soup.find_all('div',{'class':'result-info'})
    job_no=0
    npo_jobs={}

    # while True:
    #     # response = requests.get(url)
    #     data= response.text
    #     soup = BeautifulSoup(data, 'html.parser')
    #     jobs = soup.find_all('p',{'class':'result-info'})
    for job in jobs:
        # print(job)
        title= job.find('a',{'class':'result-title'}).text
        date=job.find('time',{'class':'result-date'}).text
        link = job.find('a',{'class':'result-title'}).get('href')
        #extract date/time
        date =job.find('time',{'class':'result-date'}).text
        link=job.find('a',{'class':'result-title'}).get('href')
        #in case its missing
        addressTag= job.find('span',{'class':'result-hood'})
        address= addressTag.text[1:-1] if addressTag else "N/A"
        job_response = requests.get(link)
        job_data= job_response.text
        job_soup=BeautifulSoup(job_data, 'html.parser')
        #get job description 
        job_description= job_soup.find('section' , {'id':'postingbody'}).text
        #getting things like salary and stuff 
        job_attributes_tag = job_soup.find('p',{'class':'attrgroup'})
        job_attributes=job_attributes_tag.text if job_attributes_tag else 'N/A'
        job_no +=1
        npo_jobs[job_no] = [title, address, date, link, job_attributes, job_description]
        print(f'Job Title: {title}  \nLocation {address} \nDate {date} \nLink {link} \n{job_attributes} \nJob Description {job_description} \n--------')
    # gtinfo()
    ######################Getting jobs >END< ##########################################################
    
    ######################Move to next page >START< #######################################################3
    url_tag =soup.find('a',{'title':'next page'})
    if url_tag.get('href'):
        url ='https://newyork.craigslist.org'+ url_tag.get('href')
        print(url)
    else:
        return 0        
    print("Total Jobs found:" + job_no)
    ######################Move to next page >END< #######################################################3
    #Saving output to CSV 
    npo_job_df=pd.DataFrame.from_dict(npo_jobs, orient= 'index', colums = ['Job Title', 'Address', 'Date', 'Link', 'Job attributes', 'Job Description'])
    npo_job_df.head()
    npo_job_df.to_csv('npo_jobs.csv')







def looking(look4):
    if look4 ==1:
        print("looking for links")
        getlinks()
    elif look4==2:
        print("getting title")
        title()

    elif look4 ==3:
        print("Getting locations")
        where()
    else:
        print("working on it")
        getinfo()


print("what are you looking for? \n1) Links Only \n2) Titles Only \n3) Locations Only \n4)All Possible Infomation")
x= int(input())
looking(x)

