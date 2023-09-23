# Patryk Malinowski
# Lecture 07/02/22


def read_positive_integer(question):
    num = -1
    while num < 0:
        try:
            num = int(input(question))
        except ValueError:
            print("Please provide whole numbers only.")
    return num


def read_positive_float(question):
    num = -1
    while num < 0:
        try:
            num = float(input(question))
        except ValueError:
            print("Please provide floating point numbers only.")
    return num


def read_percentage_integer(question):
    num = -1
    while 100 < num or num < 0:
        try:
            num = int(input(question))
        except ValueError:
            print("Please provide whole numbers only between 0 and 100.")
    return num


def read_percentage_float(question):
    num = -1
    while 100 < num < 0:
        try:
            num = float(input(question))
        except ValueError:
            print("Please provide whole numbers only between 0 and 100.")
    return num


def read_letters_and_spaces_only(question):
    while True:
        user_input = input(question)
        if user_input.replace(" ", "").isalpha():
            break
        else:
            print("Please provide your full name using letters and spaces only.")
    return user_input


def read_letters_spaces_and_apostrophes_only(question):
    while True:
        user_input = input(question)
        user_input = user_input.replace(" ", "")
        if user_input.replace("'", "").isalpha():
            break
        else:
            print("Please provide your full name using letters, spaces and apostrophe only.")
    return user_input


def read_yes_or_no(question):
    while True:
        user_input = input(question).lower()
        if user_input.startswith('y'):
            answer = 'Yes'
            return answer
        elif user_input.startswith('n'):
            answer = 'No'
            return answer
        else:
            print('Please respond with a Yes or No. ')


def read_letters_and_apostrophes_only(question):
    while True:
        user_input = input(question)
        if user_input.replace("'", "").isalpha():
            break
        else:
            print("Please provide your full name using letters, spaces and apostrophe only.")
    return user_input





