import sys
from app import app
from tests.data.download import get_data

if __name__ == '__main__':
    host , debug, port = 'localhost', False, 8000
    if '--host' in sys.argv:
        host = sys.argv[sys.argv.index('--host') + 1]
    if '--debug' in sys.argv:
        debug = True
    if '--port' in sys.argv:
        port = int(sys.argv[sys.argv.index('--port') + 1])
    if '--download' in sys.argv:
        get_data()
    app.run(host=host, debug=debug, port=port)