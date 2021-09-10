import json


with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['episode']:
        print(p['title'])
        
        print('')





"""

import json

data = {}
data['episode'] = []
data['episode'].append({
    'title': 'Scott',
    'image': 'stackabuse.com',
    'video': 'Nebraska',
    'category':'movies'

})

with open('data.txt', 'a') as outfile:
    json.dump(data, outfile)




"""