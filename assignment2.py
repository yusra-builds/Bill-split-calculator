# Bill Split Calculator

amount = int(input("Enter total bill amount:"))

friends = int(input("Enter total number of friends:"))

each = float(amount / friends)

print("Each person will pay:" , each)
print(type(amount) , type(friends) , type(each))