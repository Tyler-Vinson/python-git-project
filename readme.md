# Control Flow - Intro 5: The Coin Appraiser

## Objectives

By the end of this assignment you should be able to:

- Use `while` loops to repeat code based on a condition.
- Write and update loop conditions correctly to avoid infinite loops.
- Control loop flow with `break` to exit loops when needed.
- Control loop flow with `continue` to skip to the next iteration.
- Manage loop variables correctly to track state.
- Handle user input validation with loop control statements.

## Resources

- [Python `While` Loops Tutorial – YouTube](https://www.youtube.com/watch?v=rRTjPnVooxE)
- [Loop Control: break and continue – Real Python](https://realpython.com/python-keywords/#break-and-continue)
- [break vs continue – YouTube](https://www.youtube.com/watch?v=9oRqk-H3qew)

---

## Story: The Treasure Appraiser - Interactive Edition

Welcome back, Coin Appraiser! You've been promoted to **Senior Appraiser** at the Royal Treasury, and with this promotion comes a new responsibility: **real-time interactive inventory processing**.

Gone are the days of receiving entire bags of coins at once. Now, merchants from across the kingdom bring their coins **one at a time** to your window. You must:

1. **Accept each coin** as it arrives
2. **Validate immediately** (flag counterfeits)
3. **Keep a running count** so merchants see their progress
4. **Allow corrections** if a merchant changes their mind
5. **Process efficiently** without wasting the kingdom's time

The royal treasury is counting on your speed and accuracy. Merchants are waiting. Let's get to work! ⏰💰

---

## Coin Value Reference

Memorize these standard coin values:

| Coin Type | Symbol | Value  |
|-----------|--------|--------|
| Penny     | P      | $0.01  |
| Nickel    | N      | $0.05  |
| Dime      | D      | $0.10  |
| Quarter   | Q      | $0.25  |

---

## Assignment: Interactive Coin Processing with break and continue

### Assignment Description

You will write a Python program that processes coins from a merchant. For each coin:

1. **Ask the merchant** to enter a coin (P, N, D, Q)
2. **Validate the coin:**
   - If valid (P/N/D/Q): count it and show running total
   - If invalid: display warning and skip
3. **Allow early exit:** Merchant can enter 'done' to finish
4. **Display running totals** after each valid coin
5. **Show final summary** when complete

### Example

```
Welcome to the Coin Appraiser!
Enter P, N, D, or Q for each coin.
Type 'done' when finished.

Enter a coin (P, N, D, Q) or 'done': P
Running Total: 1 coins worth $0.01

Enter a coin (P, N, D, Q) or 'done': Q
Running Total: 2 coins worth $0.26

Enter a coin (P, N, D, Q) or 'done': X
Invalid coin! Please enter P, N, D, Q, or done.

Enter a coin (P, N, D, Q) or 'done': done

--- Final Summary ---
Pennies (P): 1
Nickels (N): 0
Dimes (D): 0
Quarters (Q): 1
Total Coins: 2
Total Value: $0.26

```

### Common Misconceptions/Errors to Watch Out For
- Creating an infinite loop unintentionally
- Using the wrong loop condition
- Off-by-one errors in loop boundaries
- Using = instead of == in the condition
- Modifying the loop variable incorrectly or inconsistently
- Forgetting to update the loop variable
- Misusing continue, causing skipped updates or infinite loops
- Not using break when necessary to exit the loop
- Resource mismanagement (e.g., not closing files or connections)
- Overcomplicating logic that could be handled with a for loop

### Rubric/Style Guide
- [ ] Prompts user for coins
- [ ] Uses a single while loop with proper condition
- [ ] Correctly counts each coin type
- [ ] Displays warning message for EACH unknown coin character
- [ ] Calculates total money correctly (P=0.01, N=0.05, D=0.10, Q=0.25)
- [ ] Displays summary with all coin types and total
- [ ] Output format matches example exactly (including $ and .2f formatting)
- [ ] Variables have meaningful names (index, penny_count, etc.)
- [ ] Includes appropriate comments explaining loop logic
- [ ] No infinite loops
- [ ] All test cases pass

