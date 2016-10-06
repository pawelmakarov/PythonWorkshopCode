class MyClass(object):
    def __init__(self):
        self.my_dict = {'a': 'v1', 'b': 'v2'}
        self.my_tupel = ('foo', 'bar', 'baz')
        self.my_list = ['foo', 'bar', 'baz']
        self.my_set = {'foo', 'bar', 'baz'}
        self.my_string = 'Hello World!'

ob = MyClass()

print(type(ob.my_dict))
print(type(ob.my_tupel))
print(type(ob.my_list))
print(type(ob.my_set))
print(type(ob.my_string))

print(ob.my_string[:4])
print(ob.my_string[4])
print(ob.my_string[4:])
