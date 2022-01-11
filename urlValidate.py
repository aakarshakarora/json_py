import re

def urlName(keySearch):
    url = "https://en.wikipedia.org/w/api.php?format=json&action=query&titles=" + keySearch + "&prop=revisions&rvprop=content"

    return url


def urlvalidation(URL):
    regex = re.compile(r'^(?:http|ftp)s?://'  # https:// or http://
                       r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?.)+(?:[A-Z]{2,6}.?|[A-Z0-9-]{2,}.?)|'  # domain
                       r'localhost|'  # localhost
                       r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'  # ip
                       r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, URL) is not None
