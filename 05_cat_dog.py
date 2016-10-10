class Cat(object):
	def walk(self):
		print("{0} walks alone...".format(self.__class__.__name__))

	def bark(self):
		print("Meow...")

class Dog(object):
	def walk(self):
		print("{0} walks with its master.".format(self.__class__.__name__))

	def bark(self):
		print("Gr-r-r-r-r!")

class CatDog(Cat, Dog):
	def __init__(self):
		pass


if __name__ == "__main__":
	cat = Cat()
	dog = Dog()
	cd = CatDog()

	# cat.bark()
	# cat.walk()

	# dog.bark()
	# dog.walk()

	cd.bark()
	cd.walk()
