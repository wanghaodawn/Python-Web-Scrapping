import urllib2


# Added user agent as Web Scrapping with Python
# and retry as twice when facing 5xx as response code
def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
        print html
    # Use try except to make it more robust
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        # Retry when the http code is 5xx
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e < 600:
                return download(url, user_agent, num_retries - 1)
    return html


def main():
    download('https://www.google.com')

if __name__ == "__main__":
    main()
