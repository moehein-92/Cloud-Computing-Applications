import requests
import json

url = 'https://ikm2evu584.execute-api.us-east-1.amazonaws.com/test/mp11-autograder'

payload = {
			"submitterEmail": "mhaung2@illinois.edu", # <insert your coursera account email>,
			"secret": "0lZteAmJRDIfFe2g", # <insert your secret token from coursera>,
			# "partId" : "G6U3L"
			"dbApi": "https://1rs41c06e9.execute-api.us-east-1.amazonaws.com/testing"
			
		}
print(json.dumps(payload))
r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)