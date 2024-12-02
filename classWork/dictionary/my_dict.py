my_dict = {"name":"Alice","age":25,"city":25,"city":"New York"}
#print(my_dict)

#print(my_dict["Name"])

"""if "cit" in my_dict:
	print("City is in the dictionary")
else: print("City is not in the dict")"""

"""del my_dict["city"]
print(my_dict)"""

"""print(my_dict.get("name"))
print(my_dict.get("salary","Not available"))"""

"""for dict in my_dict.values():
	print(dict, end = " ")"""
		
"""for key,value in my_dict.items():
	print(f"{key}: {value}")"""

"""squared = {x:x**2 for x in range(1,6)} 
print(squared)"""

"""def even_numb(number)
	even = {x:x**2 for x in range(1,number) if x % 2 == 0} 
	return even



keys = ["name","age","city"]
values = ["Alice",25,"New York"]

for key,value in zip(keys,values):
	my_dict[key] = value
print(my_dict)


def zip_list(my_items,size):

our_class = {}r
for key,value in zip(my_items,size)
	Our_class[key] = value
return our_class


def zip_list(my_items,size):
	#return [int(numb) for key,value in zip(my_items,size)}
	our_class = {}
	for key,value in zip(my_items,size):
		our_class[key] = value
	return our_class

def return_value(your_dict):
	for value in zip_list().values:
		return value"""


"""my_dict = {"name":"Alice","age":25}
new_data = {"city":"New York","age":26}

for key, value in new_data.items():
	my_dict[key] = value 
print (my_dict)"""


nested_dict = {
"person1": {"name":"Alice","age":25},
"person2": {"name": "Bob","age":30}
}

nested_dict["person1"]["city"] = "New York"

print(nested_dict)





	



