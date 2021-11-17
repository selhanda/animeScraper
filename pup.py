from requests import Session
from bs4 import BeautifulSoup as bs
import requests
import json


headers={"User-agent":'Mozilla/5.0 (Linux; Android 8.1.0; SM-J530F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36'}

def login():
    
    with Session() as s:
        
        site = s.get("https://freeanimes4u.000webhostapp.com/admin/login.php")
        bs(site.content, "html.parser")
        login_data = {
        "email":"#3333##33#3###33#33",
        "password":"#######3##33##33##3"
        }
        r=s.post("https://freeanimes4u.000webhostapp.com/admin/login.php",login_data,headers=headers)
        if r.status_code==200 or r.status_code==302:
            site = s.get("https://freeanimes4u.000webhostapp.com/admin/index.php")
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
            
                    next=s.post("https://freeanimes4u.000webhostapp.com/admin/addanime.php",login_data,headers=headers)
                    if next.status_code==200 or next.status_code==302:
                        print("puplishe")
                        




            
        else:
            print("rah script makhadamch makaydirch login")



login()
print("finnished")











