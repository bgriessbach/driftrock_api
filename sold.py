
#create dictionary of items:amounts sold
#return name of item with most amounts sold
def mostSold(purchases):
	itemDict = {}
	for i in purchases:
		if i["item"] in itemDict.keys():
			itemDict[i["item"]] += 1
		else:
			itemDict[i["item"]] = 1
	item = [0, None]
	for i in itemDict.keys():
		if itemDict[i] > item[0]:
			item = [itemDict[i], i]
		if itemDict[i] == item[0]:
			item.append(i)
	item = [i for i in set(item) if not str(i).isdigit()]
	if len(item) == 1:
		return item[0]
	return item
