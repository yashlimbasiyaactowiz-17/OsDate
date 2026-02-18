import  os
from datetime import datetime, timedelta,date
def dateformate(dt):
        dt = datetime.strptime(dt,"%Y-%m-%d").date()
        year = dt.year
        last_date = date(year, 12, 31)

        for i in range(1,(last_date-dt).days+1):
            folder = dt + timedelta(days=i)# 2027-01-02
            os.mkdir(fr"C:\Users\yash.limbasiya\Desktop\2027_Date_folders/{folder.strftime('%Y-%m-%d')}")

curent_date = input("enter the date 'yyyy-mm-dd': ")
dateformate(curent_date)