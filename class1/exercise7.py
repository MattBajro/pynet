
import yaml
import json
from pprint import pprint

with open("exercise6-output.yml") as f:
    yaml_list = yaml.load(f)

print "Printing out yaml list..."
pprint(yaml_list)

with open("exercise6-output.json") as f:
    json_list = json.load(f)

print "\n\nPrinting out json list..."
pprint(json_list)
