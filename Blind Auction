
print("Welcome to the secret auction.\n")
print("                                       ")

people = int(input("How many people are bidding?: "))


def highest_bid(bids):
  highest = 0
  winner = ""

  for bidder in bids:
    amounts = bids[bidder]
    amount = int(amounts)

    if amount > highest:
      highest = amount
      winner = bidder 

  print(f"The winner is {winner} with a bid of ${amount}!")


loops = 0
all_bids = {}

while loops != people:
  
  name = input("\nWhat is your name?: ")
  
  bid = input("\nWhat is your bid?: $" )
  
  loops += 1
  
  all_bids[name] = bid
  
  clear()

highest_bid(all_bids)

      

  
  
 
