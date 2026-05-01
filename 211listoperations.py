numbers = []
while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")
	choice = input("Enter choice: ")
	if choice == "1":
		num = int(input("Integer: "))
		numbers.append(num)
		print("List after adding:",numbers)
	elif choice == "2":
		if len(numbers)==0:
			print("List is empty")
		else:
			num = int(input("Integer: "))
			if num in numbers:
				numbers.remove(num)
				print("List after removing:", numbers)
			else:
				print("Element not found")
	elif choice == "3":
		if len(numbers)==0:
			print("List is empty")
		else:
			print(numbers)
	elif choice == "4":
		break
	else:
		print("Invalid choice")
