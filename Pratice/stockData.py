import requests
from datetime import datetime as dt
import time

from_date = "2020/5/5"
to_date = "2020/6/5"

F = dt.strptime(from_date, '%Y/%m/%d')
T = dt.strptime(to_date, '%Y/%m/%d')

epoch_F = int(time.mktime(F.timetuple()))
epoch_T = int(time.mktime(T.timetuple()))


url = f"https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1={epoch_F}&period2={epoch_T}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content

print(content)

with open("data.csv", 'wb') as file:
    file.write(content)

