import  os
from datetime import datetime, timedelta,date

def dateformate(dt):
    try:
        dt = datetime.strptime(dt, "%Y-%m-%d").date()
        year = dt.year
        last_date = date(year, 12, 31)
        for i in range(1,(last_date-dt).days+1):
            folder = dt + timedelta(days=i)
            os.mkdir(f"C:/Users/yash.limbasiya/Desktop/date/{folder.strftime('%Y-%m-%d')}")
        print("Your folder's has been created")
    except FileExistsError:
        print('This folders is Exists Error:FileExistsError')

curent_date = input("enter the date 'yyyy-mm-dd': ")
dateformate(curent_date)