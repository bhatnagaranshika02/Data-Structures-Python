phonebook = {
    'Anshika':999,
    'Aman':745,
    'Goru':666,

}

squares = {x: x*x for x in range(10)}

import collections
d = collections.OrderedDict(one=1,two=2,four=4)
print(d)
print(d.keys())
d['three']=3
print(d)

dd = collections.defaultdict(list)
dd['anshika'].append(993)
dd['anshika'].append(299)
dd['anshika'].append(208)

print(dd)
print(dd['anshika'])

dict1 = {'one':1 , 'two':2}
dict2 = {'three':3 , 'four':4}

chain = collections.ChainMap(dict1,dict2)
print(chain)
print(chain['four'])
#print(chain['anshika'])

read_only = collections.MappingProxyType({'one':1 , 'two':2})
print(read_only['one'])
#read_only['one'] = 23
