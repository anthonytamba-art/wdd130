# Meal Price calculator

child_price = float(input("Enter the price for a child's meal: "))
adult_price = float(input("Enter the price for an adult's meal: ")) 

children = int(input("Enter the number of children: "))
adults = int(input("Enter the number of adults: ")) 

subtotal = (child_price * children) + (adult_price * adults)    
tax = subtotal * 0.04
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")

tax_rate = float(input("Enter the tax rate (as a decimal): "))  

sales_tax = subtotal * tax_rate // 100
total = subtotal + sales_tax

print(f"Total: ${total:.2f}")
print(f"Total: ${total:.2f}")

payment = float(input("Enter the payment amount: "))
change = payment - total
print(f"Change: ${change:.2f}")
