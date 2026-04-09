tasks = []

while True:
    print("1. Add tasks\n2. View tasks\n3. Exit")

    choice = input("Enter choice : ")

    if choice == "1":
        task = input("write task :")
        tasks.append(task)

    elif choice == "2":
        for i,  item in enumerate(tasks):
            print(f"{i+1}. {item}\n")

    elif choice == "3":
        break