def calculate_change(paid, price):
    change = paid - price
    return change

snack_price = 25
print("Welcome to Snacks Vending Machine")
print("The price of the snack is: ", snack_price)
print("Accepted coins-1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Please enter coins (1, 5, 10, 25): "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin. Please insert a valid coin.")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"Insert {coin}. Total so far {total_inserted}\n.")

    if total_inserted >= snack_price:
        print("Enough money inserted!\n.")
        break

print("Dispensing your snack...\n.")
change_due = calculate_change(total_inserted, snack_price)
if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units")

print("\nPurhase Summary")
print("Snack Price: ", snack_price)
print("Total Paid: ", total_inserted)
print("Coins Inserted: ", coins_inserted)
print("Change Given: ", change_due)
print("==================================")
print("Thank you for your purchase! Enjoy your snack!")