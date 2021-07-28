
class Dictionary:
	def __init__(self, dic = {}):
		self.dic = dic

	def add(self, key, value):
		self.dic[key] = value

data = Dictionary()
data.add('Name', 'Justin')
print(data.key())
