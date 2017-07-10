#!/usr/bin/python3
import simplejson as json

# dictionaries
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry

print ("INFO: dict['Age']: ", dict['Age'])
print ("INFO: dict['School']: ", dict['School'])
print("\n")


del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary

#print ("DEBUG: dict deleted with success!")
#print ("dict['School']: ", dict['School'])

dict_watson = {
    "document_tone": {
        "tone_categories": [
            {
                "tones": [
                    {
                        "score": 0.005281,
                        "tone_id": "anger",
                        "tone_name": "Anger"
                    },
                    {
                        "score": 0.005214,
                        "tone_id": "disgust",
                        "tone_name": "Disgust"
                    },
                    {
                        "score": 0.006911,
                        "tone_id": "fear",
                        "tone_name": "Fear"
                    },
                    {
                        "score": 0.822141,
                        "tone_id": "joy",
                        "tone_name": "Joy"
                    },
                    {
                        "score": 0.02001,
                        "tone_id": "sadness",
                        "tone_name": "Sadness"
                    }
                ],
                "category_id": "emotion_tone",
                "category_name": "Emotion Tone"
            }
        ]
    }
}

# functions
def my_dict(d):
  for k, v in d.iteritems():
    if isinstance(v, dict):
      my_dict(v)
    else:
      print("{0}: {1}".format(k, v))
      print("my_dict\n")

def my_dict_v2(d):
  for k, v in d.iteritems():
    if isinstance(v, dict):
      if v['tone_categories']: my_dict(v)
      print("my_dict_v2\n")


#print ("dict['document_tone']: ", dict_watson['document_tone'])
#print(dict_watson)
#print("\n")

#my_dict(dict_watson)
#print("\n")

my_dict_v2(dict_watson)
print("\n")

print(dict_watson['document_tone'])
print("\n")

print(dict_watson['document_tone'])
print("\n")
