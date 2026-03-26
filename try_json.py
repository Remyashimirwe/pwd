# json = Javascript object notation
# python to json : json.dumps()
# json to python : json.loads()
import json
x = ('{"name":"remy",'
     '"age":15, '
     '"gender":"male"}')
y = json.loads(x)
print(y["gender"])

dict = {"name":"remy", "age":15}
j = json.dumps(dict)
print(j)
#indentation
z = json.dumps(dict, indent=2, separators=('.', '/ '))
print(z)
sort = json.dumps(dict, sort_keys=True)
print(sort)

person = {"name":"remy",
          "age":15,
          "gender":"male",
          "divorce":False,
          "address": {"street":"123", "city":"kigali"},
          "children": ["james", "jane"]
          , "siblings": ["john", "jane"]}
print(json.dumps(person, indent=2))



