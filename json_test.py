import json

with open('backup_config.json') as fh:
    conf = json.load(fh)

conf["new_key"] = 5.009
with open('backup_config.json', 'w') as fh:
    json.dump(conf, fh, indent=4, separators=(',', ':'))


print (conf)