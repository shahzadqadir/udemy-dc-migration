#!/home/sqadir/anaconda3/bin/python

import json
import requests

def pull_data(hostname, username, password, command):
	headers = {
		'content-type': 'application/json-rpc'
	}
	username = username
	password = password

	url = f"http://{hostname}/ins"
	payload = [
		{'jsonrpc': '2.0', 'method': 'cli', 'params': [command, 1], 'id':'1'}
	]

	command = json.dumps(payload)

	response = requests.post(url, data=command, headers=headers, auth=(username, password))
	return response.json()

print(pull_data('192.168.10.1', 'ans', 'cisco123', 'show ip arp'))

