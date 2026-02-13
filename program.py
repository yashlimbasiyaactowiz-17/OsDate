import  os
from datetime import datetime, timedelta,date

curent_date = datetime.today()
print(curent_date.date())
lastdate = date(2026,12,31)
print(lastdate)

avg = (lastdate-curent_date.date()).days
print(avg)
if not os.path.exists('date'):
    os.mkdir('date')

for i in range(1,avg):
    folder = curent_date + timedelta(days=i)



