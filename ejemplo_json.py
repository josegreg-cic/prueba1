
import json

json_dictio1 = '{"first_name" : "Guido", \
                "last_name"  : "Rossum"}'
json_dictio2 = '{"first_name" : "Brian", \
                "last_name"  : "Kernighan"}'

myjson_1 = json.loads(json_dictio1)

print(type(myjson_1))



x = {
    "name"  : "John",
    "age"   : 30,
    "city"  : "New York"
}

y = json.dumps(x,  indent = 4)

print(type(y))

decod = json.loads(y)

print(type(decod))
print(type(decod["age"]))


with open('base1.json','w') as outfile:
    json.dump(x, outfile)
