import  os
from datetime import datetime, timedelta,date
def dateformate(dt):
    try:
        dt = datetime.strptime(dt,"%Y-%m-%d").date()
        year = dt.year
        last_date = date(year, 12, 31)

        for i in range(1,(last_date-dt).days+1):
            folder = dt + timedelta(days=i)# 2026-01-02
            os.mkdir(f"C:/Users/yash.limbasiya/Desktop/date/{folder.strftime('%Y-%m-%d')}")

            if folder.month == 12:
                monthlast = date(folder.year,12,31)
            else :
                monthlast = date(folder.year,folder.month + 1,1)- timedelta(days=1)

            reverse_date = monthlast - timedelta(days=folder.day-1)# reverse full date ex: 2026-01-30

            f = folder.strftime('%Y-%m-%d')
            r = reverse_date.strftime('%Y-%m-%d')
            fpath = 'C:/Users/yash.limbasiya/Desktop/date/'
            exten = ['.py', '.html', '.txt', '.java']

            for ext in exten:
                with open(f"{fpath}{f}/{r}{ext}", "w"):
                    pass

        print("Your folder's has been created")
    except FileExistsError:
        print('This folders is Exists Error:FileExistsError')

curent_date = input("enter the date 'yyyy-mm-dd': ")
dateformate(curent_date)