from requests import Session
from bs4 import BeautifulSoup as bs
import requests
import json


headers={"User-agent":'Mozilla/5.0 (Linux; Android 8.1.0; SM-J530F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36'}

def login():
    
    with Session() as s:
        
        site = s.get("http://localhost:8080/anime-site/admin/login.php")
        bs(site.content, "html.parser")
        login_data = {
        "email":"codersalah0@gmail.com",
        "password":"Salah0611444831@"
        }
        r=s.post("http://localhost:8080/anime-site/admin/login.php",login_data,headers=headers)
        if r.status_code==200 or r.status_code==302:
            site = s.get("http://localhost:8080/anime-site/admin/index.php")
            bs(site.content, "html.parser")
            with open('data.json') as json_file:
                data = json.load(json_file)
                for p in data['episode']:
                    login_data = {
                       "title":p['title'],
                       "image":p['image'],
                       "video":p['video'],
                       "description":p['description'],
                       "category":p['category']
        
                    }
            
                    next=s.post("http://localhost:8080/anime-site/admin/addanime.php",login_data,headers=headers)
                    if next.status_code==200 or next.status_code==302:
                        print("puplishe")
                        




            
        else:
            print("rah script makhadamch makaydirch login")



login()
print("finnished")









"""
http://localhost:8080/anime-site/admin/addanime.php
title:
image: 
video:
category: movies
_____________________________________________________________________
login
http://localhost:8080/anime-site/admin/login.php
email: codersalah0@gmail.com
password: salah0611444831@

http://localhost:8080/anime-site/admin/index.php
"""



