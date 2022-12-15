import argparse
from app import app
from tests.data.download import LoadingCreator, download_data

if '__main__' == __name__:
    parser = argparse.ArgumentParser(description='Run the app')
    parser.add_argument('--version', action='version', version='LTL Checker 0.0.1', help='Print the version number and exit')
    parser.add_argument('--host', default='localhost', help='Host to run the app on', type=str)
    parser.add_argument('--port', default=8000, help='Port to run the app on', type=int)
    parser.add_argument('--debug', default=False, help='Run the app in debug mode', action='store_true')
    parser.add_argument('--download', default=False, help='Download test data', action='store_true')
    args = parser.parse_args()
    
    if args.download:
        with LoadingCreator(download_data) as download:
            download.run()
    
    app.run(host=args.host, debug=args.debug, port=args.port)
