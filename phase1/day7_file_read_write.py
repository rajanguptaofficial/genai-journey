with open("first_file.txt", "w") as file:
    file.write("Hum first")

with open("first_file.txt", "r") as file:
    print(file.read())  