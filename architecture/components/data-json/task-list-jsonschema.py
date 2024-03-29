import json
from jsonschema import validate
import sys

print("> start")

if len(sys.argv) < 5:
    print("invalid args")
    exit(1)

if sys.argv[3] == "-schema" and sys.argv[1] == "-data":
    data_f = sys.argv[2]
    schema_f = sys.argv[4]
elif sys.argv[1] == "-schema" and sys.argv[3] == "-data":
    data_f = sys.argv[4]
    schema_f = sys.argv[2]
else:
    print("invalid args")
    exit(1)
    
with open(data_f, 'r') as f:
    data_string = f.read()
    
with open(schema_f, 'r') as f:
    schema_string = f.read()

try:
    data = json.loads(data_string)
except Exception as e:
    print("exception invalid data string: ", e)
    exit(1)

print("> data read OK")
    
try:
    schema = json.loads(schema_string)
except Exception as e:
    print("exception invalid schema string: ", e)
    exit(1)
    
print("> schema read OK")
    
try:
    validate(data, schema)
except Exception as e:
    print("exception during validation: ", e)
    exit(1)

print("> data OK")

print("> job id " + str(data))

print("> stop")
