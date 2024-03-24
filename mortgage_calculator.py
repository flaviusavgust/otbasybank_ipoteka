def calculate_mortgage(price, intermediate_loan_reward, housing_loan_reward, down_payment=None):
    annual_interest_rate = 8.5 / 100  # Annual interest rate
    years = 20  # Loan term in years

    # Converting annual interest rate to monthly and calculating the number of payment periods
    monthly_interest_rate = annual_interest_rate / 12
    total_payments = years * 12

    # If the down payment is not specified, set it as 50% of the property price
    if down_payment is None:
        down_payment = price * 0.5

    # Calculating the loan amount after subtracting the down payment
    loan_amount = price - down_payment

    # Calculating the monthly payment using the formula for an annuity payment
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)

    # Total loan amount
    total_amount = monthly_payment * total_payments

    # Calculating the total interest paid
    total_interest = total_amount - loan_amount

    return monthly_payment, total_interest

if __name__ == "__main__":
    try:
        price = float(input("Enter the property price in tenge: "))
        intermediate_loan_reward = 5 * (price / 1000)  # Calculating the accrued reward for the Intermediate loan
        housing_loan_reward = 20 * (price / 1000)  # Calculating the accrued reward for the Housing loan
        down_payment_input = input("Enter the down payment amount in tenge (or leave it blank for 50% of the price): ")
        
        if down_payment_input == "":
            down_payment = None
        else:
            down_payment = float(down_payment_input)
        
        monthly_payment, total_interest = calculate_mortgage(price, intermediate_loan_reward, housing_loan_reward, down_payment)
        print(f"You need to accumulate an accrued reward of {intermediate_loan_reward:,.2f} tenge for the Intermediate loan.")
        print(f"You need to accumulate an accrued reward of {housing_loan_reward:,.2f} tenge for the Housing loan.")
        print(f"The monthly payment will be: {monthly_payment:,.2f} tenge.")
        print(f"The total interest paid on the loan: {total_interest:,.2f} tenge.")
    except ValueError:
        print("Error: Please enter a numerical value for the property price and down payment.")
