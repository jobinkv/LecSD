import json
import os
import requests
from tqdm import tqdm
# from ipdb import set_trace as st 

'''
Run this file from this folder. 
It will download slide images from internet and save the images as its unique ids.jpg
These unique ids helps to map its coresponding annotations.
The slide image url and is coresponding slide name are given in the files
"datastructure_slide_urls.json, computerNetworks_slide_urls.json and optimization_slide_urls.json"
The program will create a folder with name "slideImages" and save all the slide images in this folder.
'''


def download_image(url, folderName, filename):
    '''
    This function download the given url to a coresponding folder name and filename
    '''
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        with open(os.path.join(folderName,filename) , 'wb') as f:
            f.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

def slide_downloader(urlfile):
    weblinks = open(urlfile,  encoding='utf-8')
    links = json.load(weblinks)
    for item in tqdm(links):
        if item['slideUrl'][-3:]=='jpg':
            download_image(item['slideUrl'],'slideImages',item['slideName'])
    print(len(links))

slide_downloader('datastructure_slide_urls.json')
slide_downloader('computerNetworks_slide_urls.json')
slide_downloader('optimization_slide_urls.json')

