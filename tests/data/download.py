import requests, json, threading, time
from os.path import exists

"""
Load the data sources from the json file
"""
with open('tests/data/data_sources.json') as json_file:
    data_urls = json.load(json_file)['data_urls']

"""
This function is used to download test data from web sources and saves it in the app/tests/data folder.
"""
def get_data():
    thread = threading.Thread(target=_get_data)
    thread.start()

    eli_count = 0
    spinner = ['|', '/', '-', '\\']
        
    while thread.is_alive():
        print(f"{spinner[eli_count]} Loading", end='\r')
        eli_count = (eli_count + 1) % 4
        time.sleep(.2)
    thread.join()
    print('Done      ')

def _get_data():
    for data_url in data_urls:
        if exists('app/tests/data/' + data_url.split('/')[-1]):
            continue
        else:
            print('Downloading data from: (' + data_url + ')...')
            try:
                response = requests.get('https://' + data_url, timeout=10)
            except requests.exceptions.Timeout:
                print('request timed out skipping...')
                continue
            with open('tests/data/' + data_url.split('/')[-1], 'wb') as f:
                f.write(response.content)
        