#Dictionaries
student={"name":"Penguin","age":16,"Grade":12}
print(student["name"])#accesing one element
print(f"My name is {student["name"]} and I am {student["age"]}years ")#Concantination

#using loops
for key,value in student.items():
    print(f"{key}:{value}")

print(student.get("country"))