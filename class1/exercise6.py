
import yaml
import json

my_list = range(10)
my_list.append(['inside', 'list'])
my_list.append({})
my_list[-1]['ip_addr'] = '10.1.1.1'
my_list[-1]['hostname'] = 'london-rtr'

with open("exercise6-output.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open("exercise6-output.json", "w") as f:
    json.dump(my_list, f)

