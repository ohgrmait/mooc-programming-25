# Write your solution here

num = 0

my_list = []

while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "d":
        num += 1
        my_list.append(num)
    elif choice == "r":
        num -= 1
        my_list.pop(len(my_list)-1)
    elif choice == "x":
        print("Bye!")
        break
