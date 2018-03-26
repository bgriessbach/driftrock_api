from sold import mostSold
from loyal import mostLoyal

# Testing mostSold and mostLoyal functions in isolation (unit test)
# Test with small dataset, test with no dataset, test with inconclusive dataset

def testSold():
	success = []
	print("Testing mostSold(data) function with no dataset")
	data= []
	print("Input data: {}".format(data))
	print("Expected Output: None (empty)")
	print("Received Output: {}\n".format(mostSold(data)))
	success.append(mostSold(data) == None)
	
	print("Testing mostSold(data) function with small dataset")
	data= [
	{'user_id': 'FFWN-1CKR-X4WU-Q44M', 'item': 'Awesome Marble Clock', 'spend': '69.44'}, 
	{'user_id': 'HEI7-W5NW-OO9S-Z382', 'item': 'Synergistic Concrete Pants', 'spend': '9.87'}, 
	{'user_id': 'HEI7-W5NW-OO9S-Z382', 'item': 'Synergistic Concrete Pants', 'spend': '76.06'}, 
	{'user_id': 'BMCS-1VS1-39KR-7OUM', 'item': 'Durable Wool Shoes', 'spend': '66.35'}]
	print("Input data: {}".format(data))
	print("Expected Output: Synergistic Concrete Pants")
	print("Received Output: {}\n".format(mostSold(data)))
	success.append(mostSold(data) == "Synergistic Concrete Pants")

	
	print("Testing mostSold(data) function with inconclusive dataset")
	data= [
	{'user_id': 'HEI7-W5NW-OO9S-Z382', 'item': 'Synergistic Concrete Pants', 'spend': '9.87'}, 
	{'user_id': 'HEI7-W5NW-OO9S-Z382', 'item': 'Synergistic Concrete Pants', 'spend': '76.06'}, 
	{'user_id': 'BMCS-1VS1-39KR-7OUM', 'item': 'Durable Wool Shoes', 'spend': '66.35'},
	{'user_id': 'BMCS-1VS1-39KR-7OUM', 'item': 'Durable Wool Shoes', 'spend': '66.35'}]
	print("Input data: {}".format(data))
	print("Expected Output: ['Synergistic Concrete Pants','Durable Wool Shoes'] (order not guaranteed)")
	print("Received Output: {}\n".format(mostSold(data)))
	success.append(mostSold(data).sort() == ['Synergistic Concrete Pants','Durable Wool Shoes'].sort())
	print("Test Success: {}\n".format(success))	
	
def testLoyal():
	success = []
	print("Testing mostLoyal(data, users) function with no dataset")
	data= []
	users = []
	print("Input data: {} \nInput users: {}".format(data, users))
	print("Expected Output: None (empty)")
	print("Received Output: {}\n".format(mostLoyal(data, users)))
	success.append(mostLoyal(data, users) == None)	
	
	print("Testing mostLoyal(data, users) function with small dataset")
	data= [
	{'user_id': 'HEI7-W5NW-OO9S-Z382', 'item': 'Synergistic Concrete Pants', 'spend': '9.87'}, 
	{'user_id': 'HEI7-W5NW-OO9S-Z382', 'item': 'Synergistic Concrete Pants', 'spend': '76.06'}, 
	{'user_id': 'BMCS-1VS1-39KR-7OUM', 'item': 'Durable Wool Shoes', 'spend': '66.35'}]
	users = [
	{'id': 'HEI7-W5NW-OO9S-Z382', 'first_name': 'Pearlie', 'last_name': 'Yost', 'phone': '731.569.9844 x608', 'email': 'pearlie.yost@greenholt.biz'}, 
	{'id': 'BMCS-1VS1-39KR-7OUM', 'first_name': 'Travis', 'last_name': 'Kshlerin', 'phone': '(201) 847-6364 x460', 'email': 'travis_kshlerin@wunsch.net'}
	]
	print("Input data: {} \nInput users: {}".format(data, users))
	print("Expected Output: pearlie.yost@greenholt.biz")
	print("Received Output: {}\n".format(mostLoyal(data, users)))
	success.append(mostLoyal(data, users) == 'pearlie.yost@greenholt.biz')	
	
	print("Testing mostLoyal(data, users) function with inconclusive dataset")
	data= [
	{'user_id': 'HEI7-W5NW-OO9S-Z382', 'item': 'Synergistic Concrete Pants', 'spend': '9.87'}, 
	{'user_id': 'HEI7-W5NW-OO9S-Z382', 'item': 'Synergistic Concrete Pants', 'spend': '76.06'}, 
	{'user_id': 'BMCS-1VS1-39KR-7OUM', 'item': 'Durable Wool Shoes', 'spend': '66.35'},
	{'user_id': 'BMCS-1VS1-39KR-7OUM', 'item': 'Durable Wool Shoes', 'spend': '66.35'}]
	users = [
	{'id': 'HEI7-W5NW-OO9S-Z382', 'first_name': 'Pearlie', 'last_name': 'Yost', 'phone': '731.569.9844 x608', 'email': 'pearlie.yost@greenholt.biz'}, 
	{'id': 'BMCS-1VS1-39KR-7OUM', 'first_name': 'Travis', 'last_name': 'Kshlerin', 'phone': '(201) 847-6364 x460', 'email': 'travis_kshlerin@wunsch.net'}
	]
	print("Input data: {} \nInput users: {}".format(data, users))
	print("Expected Output: ['pearlie.yost@greenholt.biz', 'travis_kshlerin@wunsch.net'] (order not guaranteed)")
	print("Received Output: {}\n".format(mostLoyal(data, users)))
	success.append(mostLoyal(data, users).sort() == ['pearlie.yost@greenholt.biz', 'travis_kshlerin@wunsch.net'].sort())
	print("Test Success: {}\n".format(success))

if __name__ == "__main__":
	testSold()
	testLoyal()