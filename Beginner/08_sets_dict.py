# sets are unchangeable and no duplicates

set1 = {9,4,1,2,3,2,3}
print(set1) # note: even the num are unordered it is auto ordered

# set constructor can make sets

list1 = [1,2,3,45,4,4,7]
set2 = set(list1)
print(set2)

# accessing set is the same as list through loops and in
for x in set2:
    print(x)
# to add items to set just use .add and .remove for deleting
set1.remove(3)
set2.add(5)

print(set1,set2)

# important usefulness of set
# union or | , intersection or &, and difference or -, symettric_difference or ^

set3 = set1 | set2
print(set3)
set3 = set1 & set2
print(set3)
set3 = set1 - set2
print(set3)
set3 = set1 ^ set2
print(set3)

# dictionary or dict are key|value pairs or just 'pairs' object
dict1 = {
    'name': 'Jose',
    'age': 12,
    2: 'index'
}

# accessing them is like list or array
print(dict1['name'])

for prop in dict1:
    print(prop) # gets the list of the keys not values
    print(dict1[prop]) # gets the value of the key

for keys,values in dict1.items():
    print(keys,values)
    
for index,keys in enumerate(dict1):
    print(index,keys)
