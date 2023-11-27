import json

weblinks = open('b_OP_slides_data_final_v1.json',  encoding='utf-8')
links = json.load(weblinks)
out=[]
for item in links:
    out.append({'slideUrl':item['contentUrl'], 'slideName':item['uniqID']+'.jpg'})

with open('optimization_slide_urls.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=4)
