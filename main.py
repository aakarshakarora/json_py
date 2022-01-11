from fetchData import WorkFx
from urlValidate import UrlFx

testUrl = False
url = None
ob1 = UrlFx()
while not testUrl:
    try:
        url = input("Enter URL: ")

        if ob1.urlvalidation(url):
            testUrl = ob1.urlvalidation(url)
        else:
            print("Enter Valid Url")

    except ValueError:
        print("Enter Valid URL")
data_json = ob1.generatePyJson(url)
ob2 = WorkFx(url, data_json)
print(data_json)
pageId = ob2.getPageID()
print("Page ID of Associated Link is: " + pageId)
keyList = ob2.getSeeAlso(pageId)
print((keyList))

for value in keyList:
    print("If Key is ", value, " This URL is: ", ob1.urlvalidation(ob1.urlName(value)), ob1.urlName(value))
