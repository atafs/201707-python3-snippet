from bottle import run, get, post, request, delete
import simplejson as json
import requests


@get('/watson-api/<text>')
def getText(text):
	text_replace = text.replace(" ", "%20")

	# make the https request
	url = "https://watson-api-explorer.mybluemix.net/tone-analyzer/api/v3/tone?tones=emotion&sentences=true&version=2017-07-01&text=" + text_replace
	r = requests.get(url)
	r_text = r.text

	# writing JSON data
	data = json.loads(r_text)
	with open('data/data.json', 'w') as f:
	     json.dump(data['document_tone'], f)

	return {r_text}

run(reloader=True, debug=True)
