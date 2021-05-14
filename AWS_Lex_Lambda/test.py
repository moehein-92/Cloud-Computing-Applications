import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2"

payload = {
	"graphApi": "https://cg1caat61m.execute-api.us-east-1.amazonaws.com/testing",
	"botName": "Mapper", 
	"botAlias": "Boto", 
	"identityPoolId": "us-east-1:e681693f-fddf-4452-8a0f-19427c1f9f32", 
	"accountId": "784438638753", 
	"submitterEmail": "mhaung2@illinois.edu", 
	"secret": "KP521Ng14uH93iV0", 
	"region": "us-east-1" 
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)