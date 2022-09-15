#!/home/sqadir/anaconda3/bin/python
import json
import requests


def show_commands(hostnames, username, password, commands):
    """
    Takes a list of commands and saves raw json output in a file
    """

    headers = {
        'content-type': 'json-rpc'
    }

    for hostname in hostnames:
        url = f"http://{hostname}/ins"
        for command in commands:
            data = [
                {'jsonrpc': '2.0', 'method': 'cli',
                    'params': [command, 1], 'id':'1'}
            ]
            try:
                response = requests.post(url, headers=headers, data=json.dumps(
                    data), auth=(username, password))
                with open('outputs.txt', 'a') as afile:
                    afile.write(f"Hostname: {hostname}")
                    afile.write("\n")
                    afile.write(f"\nCOMMAND << {command} >>")
                    afile.write("\n\n")
                    afile.write(str(response.json()))
                print(
                    f"Command [{command}] outputs written to file for host {hostname}")
            except:
                print(
                    f"Host {hostname} is either not reachable or don't have NXAPI enabled")
                break


show_commands(["192.168.10.1", "192.168.10.2"], "ans", "cisco123", [
              "show ip arp", "show ip route", "show version"])
