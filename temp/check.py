import json
from ipdb import set_trace as st 


out={}
summaryv1 = json.load(open('Semantic_datav1.json', encoding='utf-8')) 
st()
splitf = json.load(open('slideLinks.json', encoding='utf-8')) 

selectedFiles = set(splitf.keys())

for item in summaryv1:
    if item in selectedFiles:
        temp = summaryv1[item]
        # del temp['glensOcr']
        out[item]=temp

with open('Semantic_datav1.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=4)