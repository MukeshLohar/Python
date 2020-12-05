# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".


# import zlib

# x = n"hello world!hello world!hello world!hello world!"
# compressed = zlib.compress(x , 9)
# print(compressed)
# print(zlib.decompress(compressed))



import zlib
s = 'hello world!hello world!hello world!hello world!'
t = str(zlib.compress(s))
print (t)
print( zlib.decompress(t))