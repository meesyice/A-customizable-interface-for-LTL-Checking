import sys

sys.path.append('.')

from data.download import get_data

def test_get_data():
    try:
        get_data()
        assert True
    except:
        assert False
