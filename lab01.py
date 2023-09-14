import requests

#print("requests libary version is: " + requests.__version__) 

resp = requests.get("https://raw.githubusercontent.com/zijing8/CMPUT404-Lab01/master/lab01.py")
print(resp.text)