# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"]
# and the object is in ["Hockey","Football"].

# Hints:
# Use list[index] notation to get a element from a list

# method1

x = ["I", "You"]
y = ["Play", "Love"]
z = ["Hockey", "Football"]

for i in range(0 , len(x) ):
    for j in range(0 , len(y) ):
        for k in range(0 , len(z) ):
            print("{} {} {}".format(x[i], y[j], z[k]))
