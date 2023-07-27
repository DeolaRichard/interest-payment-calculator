def main():
    print("This is a loan interest payment calculator")
    print(" ")

    principal = float(input("Input the Loan Amount you want: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Amount of Years: "))

    monthly_interest_payment = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_payment / (1 - (1 + monthly_interest_payment) ** (-amount_of_months))

    print(f"The monthly payment for this loan is: {monthly_payment:.2f}")

main()
