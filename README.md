# apt-data-crawler
Python web crawler framework based on Beautiful Soup html parsing and mechanize browser capabilities. Used with R to analyze apartment price data by neighborhood in the Boston area via renthop.com.

## Usage
1. You will need python3 installed on the local system
2. Create a virtual environment using `python3 -m venv /path/to/env`
  2a. Activate the virtual environment using `source /path/to/env/bin/activate`
3. Clone the repository from github using `git clone <repository_url>`
4. Move into the main project folder (`cd apt-data-crawler`) and install requirements using `pip install -r requirements.txt`
5. Run the apartment crawler script with `python renthop-crawler.py`

## Notes
The apt-data-crawler app relies on the html structure of the renthop.com website, which may be changed at any moment. Thank you for reading.

    Michael McCarthy <michemcc@outlook.com>
    https://www.linkedin.com/in/michemcc/

