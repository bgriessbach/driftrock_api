
#create dictionary user:amount of purchases
#get email of user with most purchases
def mostLoyal(purchases, users):
	userDict = {}
	if len(purchases) < 1:
		return None
	for i in purchases:
		if i["user_id"] in userDict.keys():
			userDict[i["user_id"]] += 1
		else:
			userDict[i["user_id"]] = 1
	user = [0, None]
	for u in userDict.keys():
		if userDict[u] > user[0]:
			user = [userDict[u], u]
		if userDict[u] == user[0]:
			user.append(u)
	email = [u["email"] for u in users if u["id"] in user]
	if len(email) == 1:
		return email[0]
	return email

