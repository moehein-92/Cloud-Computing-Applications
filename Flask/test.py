import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp1'

payload = {
		'ip_address1':  '35.171.22.179:8080',# <insert ip address:port of first EC2 instance>, 
		'ip_address2': '54.237.48.108:8080', # <insert ip address:port of second EC2 instance>,
		'load_balancer' : 'LB1-24371393.us-east-1.elb.amazonaws.com', # <insert address of load balancer>,
		'submitterEmail': 'mhaung2@illinois.edu',# <insert your coursera account email>,
		'secret': 'e7youghceSOXmVN4' # <insert your secret token from coursera>
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)