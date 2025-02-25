# Functions
def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
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

form_of_payment =('cash', 'credit')

want_instructions = string_check(question= "Do you want to see the instructions? ")
print(f"You chose {want_instructions}")
print()

pay_method = string_check(question="Payment Method: ", valid_ans_list= form_of_payment, num_letters=2)
print(f"You chose {pay_method}")

