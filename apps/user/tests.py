from django.test import TestCase

# Create your tests here.
import json

dict1 = '''{
    "code":1,
    "msg":"wwww",
    "is_true": True
}'''

json1 = json.dumps(dict1)

print("dict1 == ", dict1)
print("dict1 type== ", type(dict1))

print("json1 == ", json1)
print("json1 type == ", type(json1))

dict2 = json.loads(json1)

print("dict2 == ", dict2)
print("dict2 type == ", type(dict2))
