import requests
from requests.exceptions import HTTPError

response = requests.get("https://realpython.com/python-requests/")

"""
print(response.content)
print(response.text)  # to print content and text
"""
print(response.json())
if response.status_code == 200:
    print('Success..!')
elif response.status_code == 404:
    print('Not Found')

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP error occurred: {}'.format(http_err))
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success')


