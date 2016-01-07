import json
import yaml

# do tags
tagsYaml = yaml.load_all(open('tags.yaml'))
tagsJSON = []
for doc in tagsYaml:
    tagsJSON.append(doc)

json.dump(tagsJSON, open('tags.json', 'w'), indent=4, separators=(',', ': '))
