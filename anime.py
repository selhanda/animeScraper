from bs4 import BeautifulSoup
import re
import requests
import json
site = ["https://ww.anime4up.com/anime/death-note/"]
data = {}
data['episode'] = []
vidios = [] #use1
linkes = [] #use1
image=[] #USE1
titles=[] #USE1
linkestwo=""
story=[] #USE1
classname="solidfiles - HD"
description='Death Note is a story about a hardworking student, Yagami, who happens to pick up a Death Note that has been thrown from the Death God, Riku. In picking it up, we thought it was just the children'

i=1
for l in site:
    
    
    r = requests.get(l)
    soup = BeautifulSoup(r.content, "html.parser")
    for a in soup.findAll('a', attrs={'class': 'overlay'}):
        linkes.append(a.get('href'))
        
    for l in linkes:
        r = requests.get(l)           
        soup = BeautifulSoup(r.content, "html.parser")
        
        img=soup.find('img', attrs={'class': 'thumbnail'})
        image.append(img.get('src'))
        
        
        h1=soup.find('h1', attrs={'class': 'anime-details-title'})
        titles.append(h1.text)
        
        
        #p=soup.find('p', attrs={'class': 'anime-story'})
        #story.append(p.text.strip())
        #f.write(p.text.strip())
        #f.write("\n")
        #a=soup.find('a', attrs={'class': 'overlay'})
        #linkestwo=a.get('href')
        #r = requests.get(linkestwo)
        #soup = BeautifulSoup(r.content, "html.parser")
        #link=soup.find('iframe', attrs={})
        try:
            try:
                link=soup.find("a", string="solidfiles - HD")
                
        
                if classname in link.get('data-ep-url'):
                    print("try 1")
                    vidios.append(link.get('data-ep-url'))
            
            
                    data['episode'].append({
                        'title': "episode "+str(i)+" "+h1.text.strip(),
                        'image': img.get('src'),
                        'video': link.get('data-ep-url'),
                        'description': description,
                        'category':h1.text.strip()

                    })
                    print(link.get('data-ep-url'))
                    i+=1
            except:
                link=soup.find("a", string="uptostream - HD")
                
        
                if "uptostream" in link.get('data-ep-url'):
                    print("try 2")
                    vidios.append(link.get('data-ep-url'))
            
            
                    data['episode'].append({
                        'title': "episode "+str(i)+" "+h1.text.strip(),
                        'image': img.get('src'),
                        'video': link.get('data-ep-url'),
                        'description': description,
                        'category':h1.text.strip()

                    })
                    print(link.get('data-ep-url'))
                    i+=1
        except:
            print("no vidio")

    

    with open('data.json', 'a') as outfile:
            json.dump(data, outfile)
    
                

                    
                    
                      
                    
                    
    
        

    
        





