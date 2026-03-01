list=[1,1,2,2,3,3]
set1=set(list)
print(set1)
if 4 in set1:
    print("yes")
else:
    print("no")
#adding element to set

set1.add(4)
print(set1)
if 4 in set1:
    print("yes")
else:
    print("no")

#removing element from set
set1.remove(3)
set1.discard(9)
print(set1)

#operations on sets
#union operation
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a | b)
print(a.union(b))

#intersection operation
print(a&b)
a.intersection(b)

#difference in sets
a.difference(b)
print(a.difference(b))
print(a^b)
print(a.symmetric_difference(b))