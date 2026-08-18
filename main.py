print('''Welcome to the Coin Appraiser!
Enter P, N, D, or Q for each coin.
Type 'done' when finished.''')
print()
#base values for later math
number_of_coins = 0
pennies= 0.
nickel=0
dime= 0
quarter= 0
dollar = 0
two_dollar =0
coin_total=0
#loop that asks for you coin amount 
while True :
    first_coin= input("Enter a coin (P, N, D, Q, Dollar, Two Dollar) or 'done': ")
    if first_coin =='P': 
        coin_total += 0.01 
        pennies += 1
        number_of_coins += 1
        print(f"Running Total: {number_of_coins} coins worth ${coin_total:.2f}")
        print()
        continue
    if first_coin == 'N':
        coin_total += 0.05
        nickel += 1
        number_of_coins += 1
        print(f"Running Total: {number_of_coins} coins worth ${coin_total:.2f}")
        print()
        continue 
    if first_coin == 'D':
        coin_total += 0.10
        dime += 1
        number_of_coins += 1
        print(f"Running Total: {number_of_coins} coins worth ${coin_total:.2f}")
        print()
        continue 
    if first_coin == 'Q':
        coin_total += 0.25
        quarter += 1
        number_of_coins += 1
        print(f"Running Total: {number_of_coins} coins worth ${coin_total:.2f}")
        print()
        continue
    if first_coin == 'Dollar':
        coin_total += 1.00
        dollar += 1
        number_of_coins += 1
        print(f"Running Total: {number_of_coins} coins worth ${coin_total:.2f}")
        print()
        continue 
    if first_coin == 'Two Dollar':
        coin_total += 2.00
        two_dollar += 1
        number_of_coins += 1
        print(f"Running Total: {number_of_coins} coins worth ${coin_total:.2f}")
        print()
        continue 
    elif first_coin == "done":
        break    
    else:
        print('Invalid coin! Please enter P, N, D, Q, Dollar, Two Dollar, or done.')
        print()
#printing final results
print()
print("\n--- Final Summary ---")
print(f"Pennies: {pennies:.0f}")
print(f"Nickels: {nickel}")
print(f"Dimes: {dime}")
print(f"Quarters: {quarter}")
print(f"Dollars: {dollar}")
print(f"Two Dollar Bill: {two_dollar}")
print (f"Total Coins: {number_of_coins}")
print (f"Total Value: ${coin_total:.2f}")
