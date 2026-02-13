import  os
from datetime import datetime, timedelta,date

curent_date = input("enter the date '%Y-%m-%d': ")
datetime = datetime.strptime(curent_date,"%Y-%m-%d").date()
year = datetime.year
last_date = date(year, 12, 31)

def dateformate(curent_date,last_date):
    try:
        for i in range(1,(last_date-datetime).days+1):
            folder = datetime + timedelta(days=i)
            os.mkdir(f"C:/Users/yash.limbasiya/Desktop/date/{folder.strftime('%Y-%m-%d')}")
        print("Your folder's has been created")
    except FileExistsError:
        print('This folders is Exists Error:FileExistsError')
dateformate(datetime,last_date)