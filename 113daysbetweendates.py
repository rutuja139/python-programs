from datetime import datetime
date1 = input().strip()
date2 = input().strip()
date_format="%Y-%m-%d"
d1 = datetime.strptime(date1, date_format).date()
d2 = datetime.strptime(date2, date_format).date()
delta = d2-d1
print(delta.days)