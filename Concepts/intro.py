

# def hello_func(greeting, name):
#		return '{}, {}'.format(greeting, name)

# print(hello_func('Hi', 'Justin'))

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['Math', 'Art']
info = {'name' : 'John', 'age' : 22}

student_info(*courses, **info)