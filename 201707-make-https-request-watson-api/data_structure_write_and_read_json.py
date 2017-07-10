#!/usr/bin/python3

import simplejson as json
from pprint import pprint

# JSON format
data = json.loads('{"document_tone":{"tone_categories":[{"tones":[{"score":0.003768,"tone_id":"anger","tone_name":"Anger"},{"score":0.006058,"tone_id":"disgust","tone_name":"Disgust"},{"score":0.01205,"tone_id":"fear","tone_name":"Fear"},{"score":0.629505,"tone_id":"joy","tone_name":"Joy"},{"score":0.009172,"tone_id":"sadness","tone_name":"Sadness"}],"category_id":"emotion_tone","category_name":"Emotion Tone"}]}}')

# Writing JSON data
with open('data/data.json', 'w') as f:
     json.dump(data, f)

# Reading data back
with open('data/data.json', 'r') as f:
     data = json.load(f)

print (data['document_tone'])
print("\n")

pprint(data)
print("\n")

print (data["document_tone"]["tone_categories"][0]['tones'][0])
print("\n")

data_tones = data["document_tone"]["tone_categories"][0]['tones']
for array in data_tones:
    print (array['tone_name'], array['score'])

    if array['tone_name'] == 'Joy' and array['score'] > 0.5: print ('it is a positive comment\n\n')
print("\n")

a_dict = {'new_key': 'new_value'}

with open('data/data.json') as f:
    data = json.load(f)

data.update(a_dict)

with open('data/data.json', 'w') as f:
    json.dump(data, f)
