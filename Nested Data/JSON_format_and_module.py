#JSON: Java Script Object Notation


import json
# dos operaciones basicas json.loads() y json.dumps()
# json.loads(): takes a string and convertis into a dictionary/list
# json.dumps(): is the opposite of .loads(), it makes a dictionary/list into json format
#               it creates astring

# 'dumps': dump as
# 'loads': load as

# Examples

a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))




