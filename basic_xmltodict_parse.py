import xmltodict
stream = open('sample.xml','r')
xml = xmltodict.parse(stream.read())

for e in xml["People"]["Person"]:
    print(e)