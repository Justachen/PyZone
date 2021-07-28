
class Civilian:
	def __init__(self, name):
		self.name = name

	def print_name(self):
		print("My name is {}".format(self.name))

class Superhero(Civilian):
	def __init__(self, name, super_name):
		super().__init__(name)
		self.super_name = super_name

	def reveal_identity(self):
		self.print_name()
		print("... I am {}".format(self.super_name))

class Supervillian(Civilian):
	def __init__(self, name, evil_name):
		super().__init__(name)
		self.evil_name = evil_name

	def reveal_identity(self):
		self.print_name()
		print("... I am .. ehh .. {}".format(self.evil_name))



civilian1 = Civilian("Sam")

super1 = Superhero("Jack", "Lazer")
super1.reveal_identity()

evil1 = Supervillian("Max", "Deadray")
evil1.reveal_identity()