# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
# write a program to make a list whose elements are intersection of the above given lists.


element1 = [1,3,6,78,35,55]
element2 = [12,24,35,24,88,120,155]

result =[]
for i in element1 :
    for j in element2 :
        if i == j :
            result.append(i)


print(result)

#nmethod2

set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print (li)