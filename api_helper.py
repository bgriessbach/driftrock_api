import requests


#get data from endpoints
#raise error if connection fails
def getPurchases():
	with requests.Session() as s:
		data = s.get("https://driftrock-dev-test.herokuapp.com/purchases")
		if data.status_code != 200:
			raise Exception("Cannot get data", str(data.status_code))
		return data.json()["data"]

def getUsers():
	with requests.Session() as s:
		data = s.get("https://driftrock-dev-test.herokuapp.com/users")
		if data.status_code != 200:
			raise Exception("Cannot get data", str(data.status_code))
		return data.json()["data"]