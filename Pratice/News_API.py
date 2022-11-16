import requests

def get_weather(city, units='metric', api_key='26631f0f41b95fb9f5ac0df9a8f43c92'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  cont = r.json()
  return cont['list'][0]['dt_txt']

print(get_weather(city='Washington'))