import urllib.request
import json 
import re
import os
import pandas as pd

api_url= 'https://bulbapedia.bulbagarden.net/w/api.php?action=parse&format=json&page='

# Gets html from the json provided by the url
# Arg url: string url
def fetchText(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as url:
        return json.load(url)["parse"]["text"]["*"]

def remove_references(text):
    return re.sub("\[[0-9]+\]", '', text)
def fetchField(url,field):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as url:
        return json.load(url)["parse"][field]
    
def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def make_final_name(docfile):
    path, filename = os.path.split(docfile)
    filename, ext = os.path.splitext(filename)
    newfilename = f"{filename}_final{ext}"
    return os.path.join(path, newfilename)

def save_df_as_json(df, file):
    with open(file, "w", encoding="utf-8") as final_file:
        #json.dump(df.to_json(orient="index", force_ascii=False).encode("utf-8"), final_file)
        df.reset_index().to_json(path_or_buf=final_file, orient="records", force_ascii=False)
