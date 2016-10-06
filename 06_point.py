class Point(object):
	def __init__(self, x=0, y=0):
		self.__dict__['x'] = x
		self.__dict__['y'] = y
		self.__class__.last = id(object)
	# A class has a namespace implemented by a dictionary object. 
	# Class attribute references are translated to lookups in this dictionary

	last = None

	# built-in function to compute the "informal" 
		# string representation of an object.
	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)

	# __ne__() delegates to __eq__() and inverts the result 
	def __eq__(self, other):
		print 'invoke __eq__'
		return self.x == other.x and self.y == other.y

	def __ne__(self, other):
		print 'invoke __ne__'
		return not self == other
	
	# def __setattr__(self, name, value):
	# 	print 'invoke __setattr__'
	# 	if name in self.__dict__:
	# 		self.__dict__[name] = float(value)

	# def __getattr__(self, name):
	# 	print 'invoke __getattr__'
	# 	return self.__dict__[name]

	@property
	def x(self):
		print 'invoke @property'
		return self.__dict__['x']
	@x.setter
	def x(self, value):
		print 'invoke @x.setter'
		self.__dict__['x'] = float(value)

	def distance(self, other):
		from math import hypot
		return int(hypot(self.x - other.x, self.y - other.y))

if __name__ == "__main__":
    point_a = Point()
    point_b = Point(42, 42)

    print(point_a)
    print(point_b)
    print(point_a != point_b)

    point_a.x = 24
    print(point_a.x)

    print(point_a.distance(point_b))
