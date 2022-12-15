import sys

sys.path.append('.')

from data.download import download_data, LoadingCreator

def test_get_data():
    try:
        with LoadingCreator(download_data) as download:
            download.run()
        assert True
    except:
        assert False
