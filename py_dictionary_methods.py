# define a dictionary key value pair
marks={"name": "ajay",
       "age": 57,
       "kids": 2,
       "kids_name": ["ram","shyam"]}

print(marks["name"]+str(marks["age"]))

print(marks["name"]+str(marks["age"]))
print(marks["kids_name"][1])
## prints all keys
print(marks.keys())

## prints all keys with type casting
print(list(marks.keys()))

## prints all values
print(list(marks.values()))

## prints all key and values for all contents with type casting
print(list(marks.items()))

##update dicttionary by adding one more key value pair in it
updatemarks = {"address": "Jaipur"}
marks.update(updatemarks) # updating dictionary in it
print(list(marks.items())) # printing dicytionary by type casting in list


##update dicttionary by updating existing key value pair in it
updatemarks = {"address": "Delhi","kids_name":("Chinku","minku")}
marks.update(updatemarks) # updating dictionary in it
print(list(marks.items())) # printing dicytionary by type casting in list

print(marks.get("address")) # this is another method to take data from disctionary
del marks.address
print(list(marks.items())) # printing dicytionary by type casting in list
