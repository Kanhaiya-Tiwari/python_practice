dics = {
    "key" : "value",
    "name" : "kanhaiya",
    "age" : 22,
    "is adult" : True,
    "marks" : 89.8,
   "subjects" : ["maths", "science", "english"],
   "topic" : {"chapter1" : "introduction", "chapter2" : "data types"}
}
print(dics)
print(dics["name"])
dics.update({"name" : "karan"})
print(dics)
dics["age"] = 23
print(dics)
for key,value in dics.items():
    print(f"key is {key} and value is {value}")
