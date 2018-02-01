import json
from pprint import pprint

data = json.load(open('data.json'))

print data
data['maps'].append({'funy': 'not'})
with open('data_out.json', 'w') as outfile:
    json.dump(data, outfile)


persons = [
    {
        'name': 'Jan',
        'mail': 'jan@email.si'
    },
    {
        'name': 'Jakob',
        'mail': 'jakob@email.si'
    },
    {
        'name': 'Sanja',
        'mail': 'sanja@gmail.si'
    }
]

jsn_str = "[{\"name\": \"Jan\"}]"
print json.dumps(persons)
print json.loads(jsn_str)
