import pandas


# Functions
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer."

    while True:

        try:
            # Return the response if it`s an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can`t be blank. Please try again. \n")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word or the first letter 'x' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first 'x' letter
            elif response == item[:num_letters]:
                return item

        print(f"Sorry, please choose an option from {valid_answers}")


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Main Routine


# Initialize variables / non_default options for string checker
payment_ans = ('cash', 'credit')

# Ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge
CREDIT_SURCHARGE = 0.05

# lists to hold ticket details
all_names = []
all_prices = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_prices,
    'Surcharge': all_surcharges
}

# Looping
while True:
    print()

    # ask user for their name (and check if it`s not blank)
    name = not_blank("Name: ")
    if name == "xxx":
        break

    # ask for their age and check it`s between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue

    # Child price
    elif age < 16:
        ticket_price = CHILD_PRICE

    # Adult Price
    elif age < 65:
        ticket_price = ADULT_PRICE

    # Senior Price
    elif age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    pay_method = string_check(question="Payment Method: ", valid_answers=payment_ans, num_letters=2)

    if pay_method == "cash":
        surcharge = 0

    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # add name, ticket cost and surcharge to
    all_names.append(name)
    all_prices.append(ticket_price)
    all_surcharges.append(surcharge)

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total payable & profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Work out total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Output movie frame without index
print()
print(mini_movie_frame.to_string(index=False))

print()
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")
