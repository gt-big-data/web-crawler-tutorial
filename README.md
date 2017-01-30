# web-crawler-tutorial
A tutorial on making web crawlers!

Link to presentation: https://docs.google.com/presentation/d/1rK-qsNt8VyONMEGnwjkObxndMqKe8wsk0QWcxofmV84/edit?usp=sharing

## Prerequisites

* Python (2 or 3)
* `pip` (should be installed already if you have python)

## Install Dependencies

* `pip install requests beautifulsoup4`

Note for Mac and some Linux users: You might need to type `sudo` before that command.

## Is it working?

    $ cd /path/to/this/file
    $ python
    >>> from crawler import *
    Congrats! Everything is set up.

# Downloading Web Pages

Consider the GTPD non-criminal logs page:

    http://www.police.gatech.edu/crimeinfo/crimelogs/noncrimelog.html

We can download it with `get_page(MAIN_GTPD_URL)`.

After inspecting the page's source and looking at network requests, we can see that the main table with all of the logs actually comes from a completely separate request:

    http://www.police.gatech.edu/crimeinfo/crimelogs/noncrimelog.php?offset=0

We can download it directly with `get_page(GTPD_URL)`.

You can get additional pages by changing the number at the end of the URL:

    http://www.police.gatech.edu/crimeinfo/crimelogs/noncrimelog.php?offset=100
    http://www.police.gatech.edu/crimeinfo/crimelogs/noncrimelog.php?offset=200

## Complications

Sometimes network requests fail for a bunch of reasons. Maybe the server crashed, maybe it's throttling your crawler's requests, maybe you disconnected from GTWifi.

To make a crawler more robust, check the `ok` field on `requests`.

    >>> res = requests.get('http://httpstat.us/200')
    >>> res.ok
    True
    >>> res = requests.get('http://httpstat.us/500')
    >>> res.ok
    False

Sometimes, pages will require you to authenticate before viewing them. How to deal with this is completely dependent on the exact site, but `requests` definitely supports whatever you need to do. Check out all of the docs for more info:

http://docs.python-requests.org/en/master/

# Parsing Web Pages

Depending on how robust your crawler needs to be, parsing web pages can range from being super simple to rediculously complicated.

Some things to consider:

* How many different websites does the crawler need to support?
* How different are all of the pages on a site?
* What should happen if a record is missing or can't be parsed at all?
* What should happen if most of a record can be parsed but one or two fields are missing?
* What if the record has obviously wrong data (e.g. a date of "TEST")?
* What if the record has subtly wrong data (e.g. a date of 1/1/1900)?

## Basic Parser

To make life much easier, several web pages have been pre-downloaded and saved in the `pages/` folder. A very simple HTML page, `test.html` was also hand-made to demonstrate extracting data from a page.

To parse HTML, we'll use Beautiful Soup. It's very popular and makes handling HTML files much easier.

    $ python
    >>> from crawler import *
    Congrats! Everything is set up. Type `exit()` to close python.
    soup = load_page('test.html')

To extract information from the page, use `soup.select` or `soup.select_one`.

    >>> print(soup.select_one('h1').text)
    u'Wacky Waving Inflatable Arm-Flailing Tubeman Emporium'
    >>> soup.select('p')[1].text
    u'Do you know how much electricty a WWIAFT uses per hour? I have no idea.'

If you're feeling adventurous, feel free to grab data out of a much more complicated page such as `gtpd.html`.

## Advanced Parser

Heavily dependent on the exact site(s) you're crawling. Check out QDoc in the `References` section at the bottom for an actual example.

# Where to go from here?

This tutorial glossed over a few (important) details including:

* How to store all of the data you're downloading and parsing
  * Do you want to keep the raw HTML files or just the parsed information?
  * How much space will this need?
* What to do with all of the data you've acquired
  * Make a website with graphs and summaries
  * Export to CSV and play around in Excel
  * Something with "Machine Learning"
* How to glue all of the pieces together.

Check out the crawlers under `References` to see how some actual crawlers deal with all of these details.

# References

* Documentation for `requests`: http://docs.python-requests.org/en/master/
* Documentation for `beautifulsoup`: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* Documentation on CSS Selectors: https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Selectors
* Example of a simple crawler: https://github.com/gt-big-data/gtpd-crawler
  * Downloads and parses simple pages. Incomplete frontend. Stores data in MongoDB.
* Example of a more advanced crawler: https://github.com/supersam654/gatech-maintenance-requests
  * Downloads and parses simple pages. Displays data as a webpage with pretty graphs. Stores data in MonogDB but generates static files so the whole site can be hosted on GitHub Pages.
* Example of a really complicated crawler: https://github.com/gt-big-data/QDoc
  * Downloads and parses really complicated pages. Stores data in MongoDB. Data processing and visualization are handled in completely separate projects.
