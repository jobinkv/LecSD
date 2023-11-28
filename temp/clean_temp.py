import json
from ipdb import set_trace as st 



final = json.load(open('slideLinks.json', encoding='utf-8')) 
st()
# final.update(train)
# test = json.load(open('test.json', encoding='utf-8')) 
# final.update(test)
# val = json.load(open('val.json', encoding='utf-8')) 
# final.update(val)
# testCN = json.load(open('testCN.json', encoding='utf-8')) 
# final.update(testCN)
# testOpti = json.load(open('testOpti.json', encoding='utf-8')) 
# final.update(testOpti)
# st()
# print (final.keys())
# with open('slideLinks.json', 'w', encoding='utf-8') as f:
#     json.dump(final, f, ensure_ascii=False, indent=4)

ttvSplit = open('TrainTestValsplit.json',  encoding='utf-8')
splits = json.load(ttvSplit)

# dslinks = open('datastructure_slide_urls.json',  encoding='utf-8')
# links1 = json.load(dslinks) 
# cnlinks = open('computerNetworks_slide_urls.json',  encoding='utf-8')
# links2 = json.load(cnlinks) 
# cnlinks = open('optimization_slide_urls.json',  encoding='utf-8')
# links3 = json.load(cnlinks) 

# def findlink(uniqId):
#     for item in links3:
#         if item['slideName']==uniqId+'.jpg':
#             return item


# out={}
# for item in splits['testOpti']:
#     out[item]=findlink(item)
#     # out.append({'slideUrl':item['contentUrl'], 'slideName':item['uniqID']+'.jpg'})

# with open('testOpti.json', 'w', encoding='utf-8') as f:
#     json.dump(out, f, ensure_ascii=False, indent=4)
