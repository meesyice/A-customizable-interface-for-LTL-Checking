import sys
import os
import pytest

sys.path.append('.')
from app import app

@pytest.fixture(scope='module')
def client():
    return app.test_client()

class TestRoutes:

    @pytest.mark.run(order=1)
    def test_homepage(self, client):
        url = '/'
        response = client.get(url)
        assert response.status_code == 200
    
    @pytest.mark.run(order=2)
    def test_upload(self, client):
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
    
    @pytest.mark.run(order=3)
    def test_delete(self, client):
        response = client.post('/result')
        assert not os.path.exists(app.config['UPLOAD_DIRECTORY'] + '/result.xes')
        assert response.status_code == 200
    