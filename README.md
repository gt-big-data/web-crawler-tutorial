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
