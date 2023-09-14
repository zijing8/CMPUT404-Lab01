import requests

#print("requests libary version is: " + requests.__version__) 

resp = requests.get("http://google.com/")
print(resp.txt)