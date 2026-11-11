import urllib.request

url = "https://fileinfo.com/img/ss/xl/jpg_44-2.jpg"
req = urllib.request.Request(url)



# # דרך שניה
# with urllib.request.urlopen(req) as response:
#     with open("image_ilbit.jpg","wb") as file:
#         for chunk in response:
#             print(chunk)
#             chunk = response.read()
#             file.write(chunk)



def downlowd_image(req,num):
    #דרך הכי טובה 
    with urllib.request.urlopen(req) as response:      # שולח את הבקשה לשרת ופותח את התגובה שהתקבלה
        with open("image_elbitsystem.jpg", "wb") as file:  # פותח קובץ לכתיבה במצב בינארי (Bytes)

            status_code = response.status             # שומר את קוד הסטטוס של התגובה (למשל 200 = הצלחה)
            print(status_code)                        # מדפיס את קוד הסטטוס למסך
            size = 0
            while True:                               # לולאה שרצה עד שמסיימים לקרוא את כל הנתונים
                chunk = response.read(num)             # קורא 50 בתים (Bytes) בכל פעם מהתגובה
                #if not chunk:                        # אם ניגמר הבתיים
                if chunk == b"":                      # אם לא נשאר עוד מידע לקריאה
                    break                             # יוצא מהלולאה

                n = file.write(chunk)                     # כותב את 50 הבתים שנקראו לתוך הקובץ
                size += n
                print(size,end="\r")
    print()
downlowd_image(req,200)
        