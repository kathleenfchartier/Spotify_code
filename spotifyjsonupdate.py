#  This code is used to update each person's history file by adding their name to each object in the json file

import json


# Update json spotify file to add user name to streaming history

name={"name":'Corita'}

with open('Coritahistory0.json', 'r') as openfile:
    json_object=json.load(openfile)

for i in json_object:
    i.update(name)

with open('Coritahistory0.json', 'w') as closefile:
    closefile.write(json.dumps(json_object))

with open('Coritahistory1.json', 'r') as openfile:
    json_object=json.load(openfile)

for i in json_object:
    i.update(name)

with open('Coritahistory1.json', 'w') as closefile:
    closefile.write(json.dumps(json_object))
