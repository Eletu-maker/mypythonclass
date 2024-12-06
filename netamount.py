balance = 0.00
print("""welcome, pick your options
1. To deposit money
2. To redraw money
3. to check balance

Enter options """)
choice= int(input())
match choice:
	case 1:
		amount=float(input(("Enter amount ")))
		balance += amount
		print(balance)
	case 2:
		amount=float(input(("Enter amount ")))
		balance -= amount
		if balance <= 0 :
			print("insuffient fund")
	case 3:
		print("your balance is ",balance) 