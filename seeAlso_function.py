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
