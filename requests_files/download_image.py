import requests
from pathlib import Path

url = "https://hips.hearstapps.com/hmg-prod/images/gettyimages-180680638-676f621f720bc.jpg"
path = Path("dog.jpg")                # השם שאני רוצה לייצר את הקובץ 

response = requests.get(url)          # עושה בקשת GET
                                    
if response.status_code == 200:       #  אם מתקבלת בקשת status 200
    with open(path,"wb") as file:
        file.write(response.content)  #   שמירת תוכן התמונה לקובץ בפורמט בינארי 

