import sys
from app import app
from app.tests.data.download import get_data

if __name__ == '__main__':
    if len(sys.argv) > 1 and str(sys.argv[1]) == '--debug':
        get_data()
        app.run(host='localhost', debug=True, port=8000)
    else:
        app.run(host='localhost', debug=False, port=8000)