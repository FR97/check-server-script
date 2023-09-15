import json
import requests
import psutil
import os
import sys
import subprocess

def checkIfProcessRunning(processName):

    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if not checkIfProcessRunning('java'):
    subprocess.Popen(['/bin/sh', './start_server.sh'])
    slack_data = {'text': "Server was down, automatic restart completed, server is up now!"}
    webhook_url = os.getenv('NOTIFICATION_WEBHOOK_URL')
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
    sys.exit(0)

