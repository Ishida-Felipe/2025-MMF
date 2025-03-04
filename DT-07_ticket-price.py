# Fuctions
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


# Main Routine

# Initialize variables / non_default options for string checker
payment_ans = ('cash', 'credit')

#Ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge
CREDIT_SURCHARGE = 0.05

# Looping
while True:
    print()

    # ask user for their name (and check if it`s not blank)
    name = not_blank("Name: ")

    # ask for their age and check it`s between 12 and 120
    age = int_check("Age: ")

    # Output error message / sucess message
    if age < 12:
        print (f"{name} is too young")
        continue

    # Child price
    elif 12 <= age < 16:
        ticket_price = CHILD_PRICE

    # Adult Price
    elif 16 <= age < 65:
        ticket_price = ADULT_PRICE

    # Senior Price
    elif 65 <= age <= 120:
        ticket_price = SENIOR_PRICE

    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    pay_method = string_check(question="Payment Method: ", valid_answers= payment_ans, num_letters=2)

    if pay_method == "cash":
        surcharge = 0

    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    total_to_pay = ticket_price + surcharge


    print(f"{name}'s ticket cost ${ticket_price:.2f}, then paid by {pay_method} "
          f"so the surcharge is ${surcharge:.2f}\n"
          f"The total payable is ${total_to_pay:.2f}\n")

