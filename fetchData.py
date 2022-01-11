def addFx(element):
    str = ""
    for value in element:
        if value == "*" or value == "[":
            continue
        elif value != " ":
            str += value
        else:
            break

    return str


def generate_see_Also(lst):
    seeAlsolst = []
    main = "==See also=="
    mainCheck = False
    empty = ""
    for element in lst:
        if element == main:
            mainCheck = True
            print(element)

        elif mainCheck and element != empty:
            print(element)
            keyTitle = addFx(element)
            seeAlsolst.append(keyTitle)
        elif mainCheck and element == empty:
            break

    return (seeAlsolst)

class WorkFx:

    def __init__(self, url, data_json):
        self.url = url
        self.data_json = data_json

    def getPageID(self):
        temp = (self.data_json['query']['pages'])

        pageId = None
        for el in temp:
            pageId = el

        return pageId

    def getSeeAlso(self, pageId):
        temp = (self.data_json['query']['pages'])
        subURL = (temp[str(pageId)]['revisions'][0]['*'])
        lst = subURL.split('\n')
        keyList = generate_see_Also(lst)
        return keyList
