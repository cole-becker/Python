def main():
    cost_per_item = 19.99
    quantity = 5 

    # YOUR CODE FOR PART 1 GOES HERE  
    subtotal_cost = cost_per_item * quantity
    tax = subtotal_cost * 0.13
    total_cost = tax + subtotal_cost

    # YOUR CODE FOR PART 2 GOES HERE
    print(f'cost_per_item = ${cost_per_item:0.2f}') # a sample for you to use for the other prices
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')

    # THIS IS THE CODE FOR PART 3
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    
    for i in range(5):
        investment += investment * interest_rate

    print(f'After 5 years, your investment will be worth {investment} dollars.')
    # expected output: After 5 years, your investment will be worth 1187.6863056468749 dollars.

if __name__ == "__main__":
    main()