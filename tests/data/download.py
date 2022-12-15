import requests, json, threading, time
from os.path import exists

"""
a class that creates a loading animation while the data is being downloaded
"""
class LoadingCreator(object):
    def __init__(self, function) -> None:
        self.function = function
        self.spinner = ['|', '/', '-', '\\']
        self.eli_count = 0
    
    def __enter__(self):
        self.thread = threading.Thread(target=self.function)
        self.thread.start()
        return self
    
    def __exit__(self, *args) -> None:
        self.thread.join()
        print('Done            ')
    
    def run(self) -> None:
        while self.thread.is_alive():
            print(f"{self.spinner[self.eli_count]}", end='\r')
            self.eli_count = (self.eli_count + 1) % 4
            time.sleep(.2)

"""
Load the data sources from the json file
"""
with open('tests/data/data_sources.json') as json_file:
    data_urls = json.load(json_file)['data_urls']

"""
This function is used to get the test data from web sources and saves it in the app/tests/data folder.
"""
def download_data():
    for data_url in data_urls:
        if exists('tests/data/' + data_url.split('/')[-1]):
            print('Test data from: (' + data_url + ') already exists\nskipping...')
            time.sleep(.5)
            continue
        else:
            print('Test data from: (' + data_url + ') doesn\'t exist\ndownloading...')
            try:
                response = requests.get('https://' + data_url, timeout=10)
            except requests.exceptions.Timeout:
                print('request timed out skipping...')
                time.sleep(.5)
                continue
            with open('tests/data/' + data_url.split('/')[-1], 'wb') as f:
                f.write(response.content)
        