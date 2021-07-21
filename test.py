import requests

BASE = "http://192.168.43.135:5000/"

response = requests.post(BASE + "predict")
print(response)