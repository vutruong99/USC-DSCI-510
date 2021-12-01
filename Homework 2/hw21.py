def listConvert(l):
	newList = l.copy()
	res = []

	for item in newList:
		try:
			if "." not in str(item):
				res.append(abs(int(item)))
			else:
				res.append(abs(float(item)))
		except:
			continue

	return res

print(listConvert(["DSCI-510", -1, 0.1, 2, "US", 3, "-3"]))
print(listConvert([-1.0, -1.5, "-1......0", 0, "0", "0,0", "0.0", "Zero", "nega.tive"]))
print(listConvert(["Em", "co", "quen", 2, "khi", -1, "mai", -3012391289127]))