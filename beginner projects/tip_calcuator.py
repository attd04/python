// DAY 3- Tip Calculator

print("Welcome to the tip calculator\n")

#values
bbill = input("What was the total bill? $")
btip = input("How much do you want to tip? 10%, 12% or 15%? ")
bppl = input("How many people are splitting the bill? ")

# switch types
bill = float(bbill)
tip = float(btip)
ppl = float(bppl)

# calculations
# bill
tot_tip = ((tip / 100) * bill)
tot_bill = (tot_tip + bill)

# divide by people
end = round(tot_bill / ppl, 2)

print(f"Each person should pay ${end}")
