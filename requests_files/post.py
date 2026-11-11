import requests
import json
from pathlib import Path


path = Path("post_json.json")
url ="https://jsonplaceholder.typicode.com/posts"

def requests_json(url:str,path:Path)->None:
    dict_user_post = {
    "userId": 5,
    "id": 3333,
    "title": "i love",
    "body": "e"
    }

    requests_json = requests.post(url,json=dict_user_post)
    post = requests_json.json()
    with open("post_json.json","w") as file:
        json.dump(post,file,indent=4)

requests_json(url,path)