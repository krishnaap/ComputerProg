#!/usr/bin/env python3
# -*- coding: utf-8 -*-

invest_amount = int(input("Input the invest amount = "))    # Taking the input as integer     
while invest_amount <= 0 or invest_amount > 50000:          # While loop to check the condition 0 <investment amount < 50000
    print("Invalid investment amount, please re-enter the value") # investment amount is invalid
    invest_amount = int(input("Input the invest amount = ")) # variable to store an interest rate integer value input from the user in case of errors

interest_rate = int(input("Enter the interest rate (Note: desired interest rates are greater than 0 and less than 15%) = ")) #Taking user input of interest rate
while interest_rate <= 0 or interest_rate > 15:             # While loop to check the condition
    print("Invalid interest input, please enter a valid interest rate")                         # Error rate is invalid
    interest_rate = int(input("Enter the interest rate (Note: desired interest rates are greater than 0 and less than 15%) = ")) # Taking user input in case of errors

investing_duration = int(input("Enter the investing duration (Note: desired investment duration in years, must be greater than 0) = "))
while investing_duration <= 0:
    print("Invalid duration")
    investing_duration = int(input("Enter the investing duration (Note: desired investment duration in years, must be greater than 0) = ")) # Taking investing
                                                                                #duration in case of errors

#calculation 
total_months = investing_duration * 12                      # Initilize variable to convert months into years              
monthly_interest_rate = (interest_rate / 100) / 12

total_investment = 0                                        # Initilize a new variable with value zero

for month in range(1, total_months + 1):
    total_investment = total_investment+invest_amount       # Adding monthly investment amount to the total variable
    interest = total_investment * monthly_interest_rate     # interest calculation
    interest = round(interest, 2)                           # Rounding for currency
    total_investment = total_investment+interest            # Adding interest to the total investment

    if month % 12 == 0:
        current_year = month // 12
        print(f"Year {current_year}: ${round(total_investment, 2)}")

print(f"Total years calculated: {investing_duration}")
print(f"Yearly interest rate: {interest_rate}%")
print(f"Monthly investment amount: ${invest_amount}")
print(f"Total amount after compounding: ${round(total_investment, 2)}")
print("Completed by, Krishnakumar AP")


#%%
while (user_repeat := input("Want to repeat (y/n): ")) == "y":
    print("do stuff")
