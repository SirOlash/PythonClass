my_tuple = (1,2,"Olash",[5,6,7])
my_tuple [3][0] = 20
print (my_tuple)



X = ('a','b','c','d')
print(X.index('c'))

X = ('a','p','p','l','e')
print(X.count('p'))

X = ('a','p','p','l','e')
print("a"in X)

X = ('a','p','p','l','e')
print(all(X))

#X = ('a','p','p','l','e')
#for x,y in enumerate(X):
    #print(x,y)

X = ('a',2,'ciia','l','e')
print(any(X))

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, y in myfamily.items():
    print(x ,y)


