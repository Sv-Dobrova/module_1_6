my_dict = {'Sveta': 1977, 'Gera': 1974}
print(my_dict)
print(my_dict.get('Sveta'))
my_dict['son'] = 2005
print(my_dict)
my_dict.update({"daughter1": 2008,
                "daughter2": 2016})
print(my_dict)
del my_dict['son']
print(my_dict)

my_set = {1, 2, 3, 4, 1, 2, 5, "str"}
print(my_set)
my_set = {1, 2, 3, 4, 1, 2, 5, 6, 7, "str"}
print(my_set)
print(my_set.discard(1))
print(my_set)