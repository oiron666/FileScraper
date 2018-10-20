import os
import shutil
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pprint

#scraping data
url = input("Type URL\n")
while url == None:
    url = input("Type URL\n")

web_r = requests.get(url, headers={'user-agent': 'My app'})
url = "http://index-of.es/Varios-2/"
web_soup = BeautifulSoup(web_r.text, "html.parser")
driver = webdriver.Firefox()
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
file_list = []
for i in sel_soup.findAll("a"):
     href = i["href"]
     file_list.append(href)

file_list = sorted(set(file_list))
final_list = []

#assigning keywords
keywords_list = []
check = ''
while check == '':
    keyword = input("Type a keyword\n")
    keywords_list.append(keyword)
    while True:
        next_keyword = input("Do You want to add another word? y/n\n")
        next_keyword = next_keyword.lower()
        if next_keyword == "y": break
        elif next_keyword == "n":
            check = "break"
            break
        else: pass

print(keywords_list)

#getting files containg keywords
for k in keywords_list:
     for f in file_list:
         if k in f:
             print(f)
             final_list.append(f)

final_list = sorted(set(file_list))
print(final_list)

#download files
current_path = os.getcwd()

for f in final_list:
    try:
        file_name = os.path.basename(f)
        file_r = requests.get(f, stream=True)
        new_path = os.path.join(current_path, "files", file_name)
        with open(new_path, "wb") as output_file:
            shutil.copyfileobj(file_r.raw, output_file)
        del file_r
    except: pass
    time.sleep(5)
#
# iterations = 0
#
# while iterations < 10:
#     html = driver.execute_script("return document.documentElement.outerHTML")
#     sel_soup = BeautifulSoup(html, 'html.parser')
#     print(len(sel_soup.findAll("img")))
#     images = []
#     for i in sel_soup.findAll("img"):
#         src = i["src"]
#         images.append(src)
#     print(images)
#     current_path = os.getcwd()
#     for img in images:
#         try:
#             file_name = os.path.basename(img)
#             img_r = requests.get(img, stream=True)
#             new_path = os.path.join(current_path, "images", file_name)
#             with open(new_path, "wb") as output_file:
#                 shutil.copyfileobj(img_r.raw, output_file)
#             del img_r
#         except:
#             pass
#     iterations += 1
#     time.sleep(5)
#
#
#
# # driver = webdriver.Firefox()
# # driver.get(url)
