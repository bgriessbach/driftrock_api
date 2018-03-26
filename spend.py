
#get ID that matches email in user profile
#check all purchases for ID
def totalSpend(email, purchases, users):
	id = [u["id"] for u in users if u["email"] == email.lower()]
	amount = float(0)
	if len(id) < 1:
		return amount
	for item in purchases:
		if item["user_id"] == id[0]:
			amount += float(item['spend'])
	return amount