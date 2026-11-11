import requests
from pathlib import Path
import json


url = "https://jsonplaceholder.typicode.com/users"

def get_all_users(url:str):

    user_dir = Path("users")                         # תקיית users
    user_dir.mkdir(exist_ok=True)                    # אם יש תקייה כזאת אל תייצר לי

    get_requests = requests.get(url)                 # עושה בקשת get
    file_json = get_requests.json()                  # ממיר את התוצאה לגיסון

    for user in file_json:                            # עובר על הגיסון הזה
        file_name = f"{user['name']}.json"            # לוקח את השם שיש בקובץ
        file_path = user_dir / file_name              # users/לפי השם שרשום.json

        with open(file_path,mode="w") as file:
            json.dump(user,file,indent=4)

get_all_users(url)