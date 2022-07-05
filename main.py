def days_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Not supported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number, no conversion for you!")
    except ValueError:
        print("Your input is not a valid number, don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days and conversion unit!\n")
    days_and_unit = user_input.split(":")
    # print(days_and_unit)
    try:
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        validate_and_execute()
    except (IndexError, NameError):
        print("error")



