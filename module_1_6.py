my_dikt = {'Dima':1980,'Dasha':1990,'Sasha':2000,'Ilia':2010}
print(my_dikt)
print(my_dikt.get('Dima'))
print(my_dikt.get('Anya'))
my_dikt['Anya'] = 1985
my_dikt['Vitya'] = 1995
print(my_dikt)
V = my_dikt.pop('Vitya')
print(V)
print(my_dikt)
my_set = {4,5,'green','elloy',5,5,'elloy'}
print(my_set)
my_set.add(6)
my_set.add('black')
print(my_set)
my_set.discard(4)
print(my_set)