import argparse, threading, time
from app import app
from tests.data.download import get_data

if '__main__' == __name__:
    parser = argparse.ArgumentParser(description='Run the app')
    parser.add_argument('--version', action='version', version='LTL Checker 0.0.1', help='Print the version number and exit')
    parser.add_argument('--host', default='localhost', help='Host to run the app on', type=str)
    parser.add_argument('--port', default=8000, help='Port to run the app on', type=int)
    parser.add_argument('--debug', default=False, help='Run the app in debug mode', action='store_true')
    parser.add_argument('--download', default=False, help='Download test data', action='store_true')
    args = parser.parse_args()
    
    if args.download:
        thread = threading.Thread(target=get_data)
        thread.start()

        eli_count = 0
        spinner = ['|', '/', '-', '\\']
        
        while thread.is_alive():
            print(f"{spinner[eli_count]} Loading", end='\r')
            eli_count = (eli_count + 1) % 4
            time.sleep(.2)
        thread.join()
        print('Done      ')
    
    app.run(host=args.host, debug=args.debug, port=args.port)
