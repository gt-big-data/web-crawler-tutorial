import requests
from bs4 import BeautifulSoup as Soup

EXAMPLE_URL = 'http://example.com/'
GTPD_WILDCARD_URL = 'http://www.police.gatech.edu/crimeinfo/crimelogs/noncrimelog.php?offset=%d'
GTPD_URL = GTPD_WILDCARD_URL % 0
MAIN_GTPD_URL = 'http://www.police.gatech.edu/crimeinfo/crimelogs/noncrimelog.html'
GOOD_URL = 'http://httpstat.us/200'
BAD_URL = 'http://httpstat.us/500'

def get_page(url):
    res = requests.get(url)
    if not res.ok:
        print('WARNING! Could not download the requested page.')
        return ''
    return res.text

def save_page(url, filename):
    html = get_page(url)
    with open('pages/%s' % filename, 'w') as f:
        f.write(html)

def open_page(filename):
    with open('pages/%s' % filename) as f:
        html = f.read()
    return Soup(html, 'html.parser')

print('Congrats! Everything is set up. Type `exit()` to close python.')

# print(get_page(EXAMPLE_URL))
# print(get_page(GOOD_URL))
# print(get_page(BAD_URL))

# save_page(EXAMPLE_URL)
# save_page(GOOD_URL)
# save_page(BAD_URL)
