
# # when you know the range

# for i in range(7):
#     print(f"today is day {i}")

# # loop through a list

# fruits = ["Apple", "Banana", "Grapes", "Orange"]

# for item in fruits:
#     print(f"fruit name : {item}")

# # loop untill the condition is true

# i = 0

# while i <= 7:
#     print(f"{i}")
#     i += 1


# # break - stops loop completely

# for i in range(9):
#     if i == 7:
#         break
#     print(f"{i}")

# # continue - skips current iteration    

# for i in range(9):
#     if i == 7:
#         continue
#     print(f"{i}")

# # pass - does nothing (placeholder)

# for i in range(9):
#     pass

# # nested loop

# for i in range(5):
#     for j in range(4):
#         print(f"i = {i}, j = {j}")


# #  else - the else block run when the loop finishes normally (not by break)  

# for i in range(7):
#     print(f"{i}") 
# else:
#     print("done")     


# task

for i in range(10):
    print(f"{i + 1}")


i = 100

total = 0

while i > 0:
    total += i
    i -= 1

print (f"this is total {total}")

number = int(input("enter a number"))

i = 0

while i < 10:
    print(f"{number} x {i+1} = {number* (i+1)}\n")
    i += 1

