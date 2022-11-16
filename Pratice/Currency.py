import requests
from bs4 import BeautifulSoup

def currency(in_currency, out_currency, rate):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={rate}"
    print(url)
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    actual = soup.find("span", class_='ccOutputRslt').get_text()
    value = soup.find("span", class_='calOutputTS').get_text()
    print(value)
    return actual

in_currency = 'USD'  #input("Enter from place: ")
out_currency = 'INR'  #input("Enter to place: ")
amt = 1    #int(input("Enter rate: "))
print(currency(in_currency, out_currency, amt))



