import requests
import json

response = requests.get("http://216.10.245.166/Library/GetBook.php", params={'AuthorName': 'Chetan'},)
print(response.status_code)
print(response.content)
print(type(response.content))
print(type(response.text))
print(response.json()[0]['isbn'])

# for book in response.json():
#     if book['aisle'] == '343532':
#         print(book)
#         break
# expected = {'book_name': 'Postman', 'isbn': 'RS561', 'aisle': '343532'}
#
# assert book == expected