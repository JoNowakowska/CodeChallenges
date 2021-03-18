"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
For example:
    domain_name("http://github.com/carbonfive/raygun") == "github"
    domain_name("http://www.zombie-bites.com") == "zombie-bites"
    domain_name("https://www.cnet.com") == "cnet"

source: codewars.com
"""

def domain_name(url):
    http_www_id = url.find('http://www.')
    https_www_id = url.find('https://www.')
    http_id = url.find('http://')
    https_id = url.find('https://')
    www_id = url.find('www.')

    if http_www_id == 0:
        url = url[11:]
    elif https_www_id == 0:
        url = url[12:]
    elif http_id == 0:
        url = url[7:]
    elif https_id == 0:
        url = url[8:]
    elif www_id == 0:
        url = url[4:]

    domain_end_id = url.find('.')

    url = url[:domain_end_id]

    return url

print(domain_name("http://github.com/carbonfive/raygun"))


# the highest rated solution:
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


# another nice solution by gridgrd:
def domain_name(url):
    url = url.replace('www.', '')
    url = url.replace('https://', '')
    url = url.replace('http://', '')

    return url[0:url.find('.')]