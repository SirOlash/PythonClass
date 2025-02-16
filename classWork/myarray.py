class MyArray:
   # def __init__(self):  #Constructor
    #    pass
    def __init__(self,size): #Constructor
        self.size =size
        self.capacity = size
        self.my_array = [] * size

    def is_empty(self):
        return self.size == 0





#MyArray m1 = new MyArray()
first_array = MyArray(5) #Instance like java above
first_array.is_empty()


