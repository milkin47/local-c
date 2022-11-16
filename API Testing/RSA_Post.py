import requests
import json
from payload import *
import configparser
from Utilities.configurations import getconfig
from Utilities.Resources import APIresources

print("---POSTBook")
url_addBook = getconfig()['API']['endpoint'] + APIresources.addBook
print(url_addBook)
response = requests.post(url_addBook, json=addbookpayload("12345"),)
print(response.status_code)
print(response.json())

Id = response.json()['ID']
print(Id)
print("-----GetBook-------")
url_getBook = getconfig()['API']['endpoint'] + APIresources.getBook
params = {'ID': Id}
response_get = requests.get(url_getBook, params=params)
print(response_get.status_code)
print(response_get.json())

print("------Deletebook---------")
url_deleteBook = getconfig()['API']['endpoint'] + APIresources.deleteBook
json_id = {"ID": Id}
response_delete = requests.delete(url_deleteBook, json=json_id,)
print(response_delete.status_code)
print(response_delete.json())
