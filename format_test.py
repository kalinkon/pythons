print('{:>10}'.format('test'))

# output
      # test
print('{}'.format('test'))

print('{:.5}'.format('xylophone'))

print('{:f}'.format(3.141592653589793))


i=22
x=7
pai=i/x
print(pai)
print(type(pai))

print('{:f}'.format(pai))

print('{:06.2f}'.format(3.141592653589793))

print('{:+d}'.format(42))

data = {'first': 'Hodor', 'last': 'Hodor!','third':'fu!'}
print('{first} {last} {third}'.format(**data))

print('{d[first]} {d[last]} {d[third]}'.format(d=data))

class Plant(object):
    type = 'tree'
print('{p.type}'.format(p=Plant()))