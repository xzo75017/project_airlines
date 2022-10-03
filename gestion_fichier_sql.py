import json

def json_file():
    #lecture + Chargement des fichiers 
    jdata = [json.loads(line) for line in open('vol13_json', 'r')]
    jdata2 = [json.loads(line) for line in open('price2_json', 'r')]
    jdata3 = [json.loads(line) for line in open('event_json',encoding='utf8')]
    jdata4 = [json.loads(line) for line in open('airport_json', 'r')]
    jdata5 = [json.loads(line) for line in open('airlines_json', 'r')]