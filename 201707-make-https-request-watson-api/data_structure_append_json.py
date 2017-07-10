import simplejson as json

a_dict = {'new_key': 'new_value'}

with open('data/test.json') as f:
    data = json.load(f)

data.update(a_dict)

with open('data/test.json', 'w') as f:
    json.dump(data, f)
