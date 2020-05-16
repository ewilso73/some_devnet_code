import yaml
from yaml import load, load_all
stream = open('sample2.yaml','r')
documents = load_all(stream, Loader=yaml.FullLoader)

for doc in documents:
    print(doc['people'][0])

#run with python NOT python3