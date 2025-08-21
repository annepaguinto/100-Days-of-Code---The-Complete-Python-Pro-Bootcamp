import art
print(art.logo)
active_bidding = True
price = {}
compare = []
highest = 0
winner = ""
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

while active_bidding:
    name = input("What is your name?:")
    bid_amount = int(input("What is your bid?:"))
    price[name] = bid_amount
    compare.append(bid_amount)
    highest = max(compare)
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

    if other_bidders == 'no':
        active_bidding = False

    for joiner in price:
        if price[joiner] == highest:
            winner = joiner


print(f"The winner is {winner} with a bid of ${highest}")

