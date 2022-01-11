import re
from urllib.request import urlopen
import json


class UrlFx:

    def urlName(self, keySearch):
        """
        This method will return url wrt to key element and it will be injected in dummy link to generate associated json file

        :param keySearch:
        :return:
        """
        url = "https://en.wikipedia.org/w/api.php?format=json&action=query&titles=" + keySearch + "&prop=revisions&rvprop=content"

        return url

    def urlvalidation(self, URL):
        """
        This method primarily check if URL is valid or not
        :param URL:
        :return:
        """
        regex = re.compile(r'^(?:http|ftp)s?://'  # https:// or http://
                           r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?.)+(?:[A-Z]{2,6}.?|[A-Z0-9-]{2,}.?)|'  # domain
                           r'localhost|'  # localhost
                           r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})'  # ip
                           r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, URL) is not None

    def generatePyJson(self, url):
        """
        This method will fetch data from JSON file and will convert to data of dict type

        :param url:
        :return:
        """
        response = urlopen(url)
        data_json = json.loads(response.read())

        return data_json
