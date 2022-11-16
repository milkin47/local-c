import requests
from Utilities.configurations import getpassword

print("----Using Auth---------")
url_git = "https://api.github.com/milkin47"           # "https://api.github.com/user"
response_git = requests.get(url_git, verify=False, auth=('milkin47', getpassword()), )
print(response_git.status_code)
response_git.close()

url_git2 = "https://api.github.com/users/repos"
response_git2 = requests.get(url_git2)  #, verify=False, auth=('milkin47', getpassword()), )
print(response_git2.status_code)
response_git2.close()

print("------Using Cookies------")
# se = requests.session()
# se.cookies.update({'visit-year':'2022'})
# url_bin = "https://httpbin.org/cookies"
# respose_bin = se.get(url_bin, cookies={'visit-month':'March'})
# print(respose_bin.status_code)
# print( respose_bin.text)

print("---Blocking re-direction and giving timeout------")
response_rahul = requests.get("http://rahulshettyacademy.com", allow_redirects=False, timeout=3)
print(response_rahul.history)
print(response_rahul.status_code)

print("------uploading file-----")
file = {'file': open(r"C:\Users\Milky\Documents\API testing test image.png", 'rb')}
response_png = requests.post("https://petstore.swagger.io/v2/pet/9843217/uploadImage", files=file)
print(response_png.status_code)
print(response_png.text)