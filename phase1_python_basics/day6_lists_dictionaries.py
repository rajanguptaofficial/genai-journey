# lists

fruits = ["Apple", "Banana", "Orange", "Mango"]
numbers = [1, 2, 3, 4, 5, 6, 7]

fruits.append("Water Melon")

print(f"these are append {fruits}")

fruits.insert(2, "Cherry")

print(f"these are insert {fruits}")

fruits.remove("Water Melon")

print(f"these are remove {fruits}")

fruits.pop()

print(f"these are pop {fruits}")

# slicing

print(fruits[0:2])


# dictionaries

student = {
    "name" : "Rajan",
    "age" : 22,
    "course" : "AI"
}

student["city"] = "Delhi"

print(f"add key {student}")

student.pop("age")

print(f"remove key {student}")

for key, value in student.items():
    print(f"student info  {key} : {value}")


