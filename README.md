# apt-data-crawler
Python web crawler framework based on Beautiful Soup html parsing and mechanize browser capabilities. Used with R to analyze apartment price data by neighborhood in the Boston area via renthop.com.

## Usage
1. You will need python3 installed on the local system
2. Create a virtual environment using `python3 -m venv /path/to/env`
3. Activate the virtual environment using `source /path/to/env/bin/activate`
4. Clone the repository from github using `git clone <repository_url>`
5. Move into the main project folder (`cd apt-data-crawler`) and install requirements using `pip install -r requirements.txt`
6. Run the apartment crawler script with `python renthop-crawler.py`

## Notes
The apt-data-crawler app relies on the html structure of the renthop.com website, which may be changed at any moment. Thank you for reading.

    Michael McCarthy <michemcc@outlook.com>
    https://www.linkedin.com/in/michemcc/

