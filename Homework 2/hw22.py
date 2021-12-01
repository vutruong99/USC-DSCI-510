def read_csv(filename):
	table = dict()
	handler = open(filename, "r", encoding = "utf-8-sig")
	data = []

	for i,line in enumerate(handler):
		if i == 0:
			headers = line.rstrip().split(",")
		else:
			data.append(line.rstrip().split(","))

	column = -1

	for header in headers:
		table[header] = []
		column = column + 1
		for i in range(0,len(data)):
			table[header].append(data[i][column])

	print(table)

	return table

read_csv("Students_Q2Q3.csv")
