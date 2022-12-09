# A-customizable-interface-for-LTL-Checking
A-customizable-interface-for-LTL-Checking created for the Process Conformance Checking in Python Praktikum

## Installation
- **Windows** - Run through Docker
1. [Clone this repo](https://help.github.com/en/articles/cloning-a-repository) with git.
2. Run `docker run -it $(docker build -q .)` within the directory that you cloned (probably `A-customizable-interface-for-LTL-Checking`).
3. Open the development site by going to [`http://127.0.0.1:8000`](http://127.0.0.1:8000) in your browser.

- **Linux or macOS** - Run directly
1. [Clone this repo](https://help.github.com/en/articles/cloning-a-repository) with git.
2. Run `python run.py` within the directory that you cloned (probably `A-customizable-interface-for-LTL-Checking`).
3. Open the development site by going to [`http://localhost:8000`](http://localhost:8000) in your browser.

## **Run flags**

1. '--debug' to run the program in debug mode
2. '--download' to download some test data
3. '--version' to print the version number and exit
4. '--port' to set a custom port. Default port is 8000.
5. '--host' to set a custom hostname. Default hostname is localhost.

## **Authors**
Mohammed Al-Laktah
Fares Motia
Saad Safan
Ping Wu

## **License**
This project is licensed under the GNU General Public License v3.0 - see the [`LICENSE`](LICENSE) file for details.
