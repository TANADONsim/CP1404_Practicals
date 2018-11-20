total_price = []
num_items = int(input("Enter the number of items purchased"))
for i in range(1, num_items + 1, 1):
    print("Please enter price of item", i)
    item_price = float(input())
    if item_price < 0:
        print("Invalid price. Please try again.")
        total_price = []
        break
    print("Price of item: $", item_price)
    total_price.append(item_price)

amount_payable = sum(total_price)

if amount_payable >= 100:
            amount_payable = amount_payable * 0.9

print("Please pay $", amount_payable)
