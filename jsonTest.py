import json


sample = {					
"rank":1, "name":"OH" , "number":868
}					

a = open('sample.json', 'w')
json.dump(sample, a)
a.close()

b = open('sample.json')
c = json.load(b)

print (c)