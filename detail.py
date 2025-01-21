"""num = 5 #variable - allows storing one value
num = [2,55,66,4,77]  - #allows storing multiple values
num = [] - #empty list
"""
#dictionaries
sample_dict = {}

student = {
    "name" : "aarush",
    "age" : 11,
    "city" : "mycity"
}
print(student)

#a list with same details to see difference
sample_list = ["Aarush",11,"mycity"]
print(sample_list)

 #access key
print(student.keys())

#access values
print(student.values())






#to print all key and value pair together 
for key in student.keys():
    print(key, student[key])

#print any particular value
print(student["name"])

#to check whether key is present or not
if "country" in student :
    print(student["country"])

else :
    print ("key is not present")

if "city" in student :
    print(student["city"])

else :
    print ("key is not present")

#delete  a key-value pair
del student["city"]
print(student)


#add a new key value pair
student["country"] = "UK"
print(student)

#how to change an existing value
student["age"]  = 10
print(student["age"]) #print only the age from the dictionary

#store a list in the dictionary
student["marks"]= [70,85,91,62,89]

#access the third element(index=2) from the list marks from dictionary
print(student["marks"][2])

print(student["marks"][4])


#nested dictionary
#nested dictionary - key(name) : value (dictionary with details)
student={
    "aarush" : {
        "age" : 11,
        "city" : "mycity"
},

"shalini" : {
    "age" : 30,
    "city" : "mycity1"
}
}

print(student)

#print keys
print(student.keys())

#print values
print(student.values())

#change value
student["shalini"]["age"] = 29
print(student["shalini"])
#length of dictionary = no keys - value pair
print(len(student))

