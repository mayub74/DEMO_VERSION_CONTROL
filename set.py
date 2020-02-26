#python code to create two set find out.......
#union ,intersection,difference bet this two sets.
s1={2,4,3,1,5,2,}
s2={0,7,5,3,1,9,7}
# removes duplicate elements
print("set 1 :",s1)
print("set 2 :",s2)
print("union :",s1|s2)
print("intersection is:",s1&s2)
#elements in first set which are not in second set
print("difference s1-s2 is:",s1-s2)
print("difference s2-s1 is:",s2-s1)

print("symmetric difference is:",s1^s2)
