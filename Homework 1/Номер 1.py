import re
from urllib.parse import urlparse


def domain_name(url):
    if not re.match(r'http:', url) and not re.match(r'https:', url):
        url = 'http://' + url
    url = urlparse(url)
    url = url.netloc.split('.')
    return url[1] if url[0] == 'www' else url[0]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
