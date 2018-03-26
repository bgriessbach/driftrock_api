import sys
from api_helper import getPurchases, getUsers
from sold import mostSold
from loyal import mostLoyal
from spend import totalSpend

def main():
	#input validation
	#check which command is requested and if all required parameters exist
	if len(sys.argv) < 2:
		raise Exception("Please enter command 'most_sold', 'total spend [EMAIL]' or 'most_loyal'")

	elif sys.argv[1].lower() == "most_sold":
		purchases = getPurchases()
		item = mostSold(purchases)
		return print(item)

	elif sys.argv[1].lower() == "most_loyal":
		purchases = getPurchases()
		users = getUsers()
		email = mostLoyal(purchases, users)
		return print(email)

	elif sys.argv[1].lower() == "total_spend":
		if len(sys.argv) < 3 or "@" not in sys.argv[2]:
			raise Exception("Not a valid email provided")
		purchases = getPurchases()
		users = getUsers()
		email = sys.argv[2].strip()
		amount = totalSpend(email, purchases, users)
		return print(amount)

	else:
		raise Exception("Not a recognised command. Please enter command 'most_sold', 'total spend [EMAIL]' or 'most_loyal'")

if __name__ == "__main__":
    main()