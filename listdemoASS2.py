#code to create a list to perform
#insert ,append ,extend ,remove  functions on it.
l1=[2,'w','q',9.9]
print("list content :",l1)
l1.insert(3,5)
print("list content after insert :",l1)
l1.append('d')
print("list content after append :", l1)
l1.remove('q')
print("list content after removing 'q' :",l1)
print("list content after pop() :",l1.pop())
l2=[2,3,4]
l1.extend(l2)
print("list content after extend() :",l1)
