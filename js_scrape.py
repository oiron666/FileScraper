import os
import shutil
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pprint


url = "http://index-of.es/Varios-2/"
web_r = requests.get(url, headers={'user-agent': 'My app'})
web_soup = BeautifulSoup(web_r.text, "html.parser")
#
# driver = webdriver.Firefox()
# driver.get(url)
#
# html = driver.execute_script("return document.documentElement.outerHTML")
#
# sel_soup = BeautifulSoup(html, 'html.parser')
# pdf = []
#
#
# for i in sel_soup.findAll("a"):
#     href = i["href"]
#     pdf.append(href)

keywords_list = []
check = ''
while check == '':
    keyword = input("Type a keyword\n")
    #next_keyword = 'y'
    while True:
        next_keyword = input("Do You want to add another word? y/n\n")
        next_keyword = next_keyword.lower()
        keywords_list.append(keyword)
        if next_keyword == "y": break
        elif next_keyword == "n":
            check = "break"
            break
        else: pass





#print(pdf[23])
pdf = sorted(set(pdf))

#print(pdf(i))
for i in pdf:
    #print(i)
    if 'Python' in i:
        print(i)

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
