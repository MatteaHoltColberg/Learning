def saving_for_house():
    ''' Receives annual salary, percent to save, and cost of home 
        as inputs. Returns number of months it will take to save 
        for a 25% down payment with a 4% savings rate. 
    '''
    annual_salary = float(input("Enter your annual salary: "))
    monthly_salary = annual_salary/12
    portion_down_payment = 0.25
    current_savings = 0.00
    r = 0.04
    monthly_return = 1 + (r/12)
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    months = 0

    # While the user's savings don't cover the down payment:
    while current_savings < (portion_down_payment * total_cost):

        # Add the monthly return.
        # Then add saved portion of the monthly salary to savings.
        current_savings *= monthly_return
        current_savings += (monthly_salary * portion_saved)

        # Add one month.
        months += 1

    # Return how many months it takes to save enough.
    return months

def saving_with_raise():
    ''' Receives starting annual salary, percent to save, cost 
        of home, and semi-annual raise as inputs. Returns number 
        of months it will take to save for a 25% down payment 
        with a 4% savings rate. 
    '''
    annual_salary = float(input("Enter your annual salary: "))
    monthly_salary = annual_salary/12
    portion_down_payment = 0.25
    current_savings = 0.00
    r = 0.04
    monthly_return = 1 + (r/12)
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter your semi-annual raise, as a decimal: "))
    months = 0.00

    # While the user's savings don't cover the down payment:
    while current_savings < (portion_down_payment * total_cost):

        # If months/6 is an integer, give the semi-annual raise.
        if months > 0 and (months/6) == int(months/6):
            annual_salary *= (semi_annual_raise + 1)
            monthly_salary = annual_salary/12
            
        # Add the monthly return.
        # Then add saved portion of the monthly salary to savings.
        current_savings *= monthly_return
        current_savings += (monthly_salary * portion_saved)

        # Add one month.
        months += 1

    # Return how many months it takes to save enough.
    return months

def amount_to_save():
    ''' Receives starting annual salary. Returns best percent 
        to save for the down payment in 36 months and steps in 
        bisection search given a 7% semi-annual raise, a 4% 
        savings rate, a 25% down payment, and a $1M house.
    '''

print("Number of months: {}".format(saving_with_raise()))

