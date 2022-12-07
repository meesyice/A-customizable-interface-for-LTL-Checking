import sys

sys.path.append('.')
from app import app

def test_homepage():
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200