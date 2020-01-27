import requests
import getpass

BASE_URL = 'http://IP_ADDRESS:5000/webapi/'
USERNAME = 'user'
API_AUTH = '6'
API_DS = '3'


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_api_versions():
    r = requests.get(BASE_URL + 'query.cgi?api=SYNO.API.Info&version=1&method=query&query=SYNO.API.Auth,'
                                'SYNO.DownloadStation.Task')
    return r.json()


def api_login():
    password = getpass.getpass("Please enter the password for username " + USERNAME + ": ")

    with requests.Session() as s:
        s.get(BASE_URL + 'auth.cgi?api=SYNO.API.Auth&version=' + API_AUTH + '&method=login&account=' + USERNAME + '&passwd=' + password + '&session=DownloadStation&format=cookie')
    return s


def get_tasks(session):
    r = session.get(BASE_URL + 'DownloadStation/task.cgi?api=SYNO.DownloadStation.Task&version=' + API_DS + '&method=list'
                               '&additional=tracker')
    for task in r.json()['data']['tasks']:
        if 'additional' in task:
            if 'tracker' in task['additional']:
                for tracker in task['additional']['tracker']:
                    if tracker['status'] != 'Success':
                        print(BColors.OKBLUE + BColors.BOLD + task['title'] + BColors.ENDC, task['additional']['tracker'])


get_tasks(session=api_login())
