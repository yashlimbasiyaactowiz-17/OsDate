import  os
from datetime import datetime, timedelta,date

def dateformate():
    curent_date = datetime.today()
    lastdate = date(2026,12,31)

    if not os.path.exists('date'):
        os.mkdir('date')
    for i in range(1,(lastdate-curent_date.date()).days):
        folder = curent_date + timedelta(days=i)
        os.mkdir(f"date/{folder.strftime('%Y-%m-%d')}")

dateformate()