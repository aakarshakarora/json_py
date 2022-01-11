from urllib.request import urlopen
import json
from seeAlso_function import generate_see_Also
from urlValidate import urlvalidation, urlName

keySearch = "SMALL"
url = urlName(keySearch)
print("Current URL is: ", urlvalidation(url))

response = urlopen(url)
data_json = json.loads(response.read())
temp = (data_json['query']['pages'])

pageId = None
for el in temp:
    pageId = el

print("Page ID of Associated Link is: " + pageId)

subURL = (temp[str(pageId)]['revisions'][0]['*'])
lst = subURL.split('\n')
keyList = generate_see_Also(lst)
print("Search Key: " + str(keyList))

for value in keyList:
    print("If Key is ", value, " This URL is: ", urlvalidation(urlName(value)), urlName(value))
