class lol():
	default = []

	def __init__(self, name):
		self.name = name


	def changeDefault(self):
		self.default.append("VCL")

lol1 = lol("TEN TAO LA VU")
print(lol1.name)
print(lol.default)
lol1.changeDefault()
print(lol1.default)

lol2 = lol("notVu")
print(lol2.name)
print(lol2.default)
