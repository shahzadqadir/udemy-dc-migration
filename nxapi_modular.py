#!/home/sqadir/anaconda3/bin/python

import json
import requests


def show_commands(hostname, username, password, commands):
    command_counter = 1
    """Takes a list of commands ans push them to device, 
    one by one and prints output to screen"""
    url = f"http://{hostname}/ins"
    headers = {'content-type': 'application/json-rpc'}

    for command in commands:
        data = [
            {'jsonrpc': '2.0', 'method': 'cli',
                'params': [command, 1], 'id':'1'}
        ]
        response = requests.post(url, headers=headers, data=json.dumps(
            data), auth=(username, password))
        with open('commands_output.txt', 'a') as wfile:
            wfile.write(f"output of command {command}")
            wfile.write(str(response.json()))
            wfile.write("\n")


show_commands("192.168.10.1", "ans", "cisco123", [
              "show ip int brief", "show ip route", "show ip arp"])
