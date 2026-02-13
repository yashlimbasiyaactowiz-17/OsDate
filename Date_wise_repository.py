import  os
from datetime import datetime, timedelta,date

curent_date = datetime.today()
last_date = date(2026, 12, 31)

def dateformate(curent_date,last_date):
    try:
        for i in range(1,(last_date-curent_date.date()).days):
            folder = curent_date + timedelta(days=i)
            os.mkdir(f"C:/Users/yash.limbasiya/Desktop/date/{folder.strftime('%Y-%m-%d')}")
        print("Your folder's has been created")
    except FileExistsError:
        print('This folders is Exists Error:FileExistsError')
dateformate(curent_date,last_date)