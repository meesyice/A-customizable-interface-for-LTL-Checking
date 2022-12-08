import sys

sys.path.append('.')
from app import app

def test_homepage():
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200
    
def test_upload():
    client = app.test_client()
    file_name = 'running-example.xes'
    datei = {
        'datei': (open('tests/data/running-example.xes','rb'), file_name),
        'LTL_rule_1':'A eventually B',
        'activitiesOfThefirstRule':['decide', 'check ticket'],
        'andOr':'none'
    }
    response = client.post('/upload', data=datei, content_type='multipart/form-data')
    assert response.status_code == 302
    
    