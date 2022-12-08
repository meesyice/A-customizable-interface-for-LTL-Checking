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
    file = open('tests/data/running-example.xes','rb')
    datei = {
        'datei': (file, 'running-example.xes'),
        'LTL_rule_1':'A eventually B',
        'activitiesOfThefirstRule':['decide', 'check ticket'],
        'andOr':'none'
    }
    response = client.post('/upload', data=datei, content_type='multipart/form-data')
    file.close()
    assert os.path.exists(app.config['UPLOAD_DIRECTORY'] + '/result.xes')
    assert response.status_code == 307
    
def test_delete():
    client = app.test_client()
    response = client.post('/result')
    assert not os.path.exists(app.config['UPLOAD_DIRECTORY'] + '/result.xes')
    assert response.status_code == 200
    