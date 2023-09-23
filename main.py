# Patryk Malinowski
# R00210173
# Project Holiday Camp 2022

import validating_user_inputs

KIDS_COST = 100
POOL_COST = 150
BOOKING_LIMIT = 30


def read_bookings_file(filename):
    accommodation = []
    price = []
    old_bookings = []
    with open(filename) as data:
        for line in data:
            line_list = line.split(",")
            accommodation.append(line_list[0])
            price.append(float(line_list[1]))
            old_bookings.append(int(line_list[2]))
    total_old_bookings = sum(old_bookings)
    return accommodation, price, old_bookings, total_old_bookings


def update_bookings_file(filename, accommodation, price, new_bookings):
    i = 0
    number_of_lines = len(accommodation)
    with open(filename, "w") as connection:
        while i < number_of_lines:
            print(f"{accommodation[i]},{price[i]},{new_bookings[i]}", file=connection)
            i += 1


def read_extras(filename):
    extra = []
    bookings = []
    with open(filename) as data:
        for line in data:
            line_list = line.split(",")
            extra.append(line_list[0])
            bookings.append(int(line_list[1]))
    return extra, bookings


def save_extras(total_kids_camp, total_pool_pass, total_people, filename):
    pool_pass = validating_user_inputs.read_yes_or_no("Do you require a family pool pass (Yes/No)? ")
    current_kids_camp = validating_user_inputs.read_positive_integer("How many kids will join the kids club? ")
    while total_people <= current_kids_camp:
        print(f"Your No. of kids booked in must be less than the {total_people} total people in your group. ")
        current_kids_camp = validating_user_inputs.read_positive_integer("How many kids will join the kids club? ")
    if pool_pass.startswith("Yes"):
        current_pool_pass = 1
    else:
        current_pool_pass = 0
    total_kids_camp += current_kids_camp
    total_pool_pass += current_pool_pass
    with open(filename, "w") as connection:
        print(f"Kids Camp,{total_kids_camp}", file=connection)
        print(f"Pool Pass,{total_pool_pass}", file=connection)
    return pool_pass, current_kids_camp, current_pool_pass


def menu():
    print('LONG ISLAND HOLIDAYS')
    print('====================')
    print('1. Make a Booking')
    print('2. Review Bookings')
    print('3. Exit')
    print()
    choice = int(input("Please choose one of the above options ===> "))
    while choice > 3 or choice < 1:
        try:
            choice = int(input("Please choose one of the above options ===> "))
        except ValueError:
            print("Please choose between option 1, option 2, option 3. ")
    return choice


def booking():
    accommodation, price, old_bookings, total_old_bookings = read_bookings_file("bookings_2022.txt")
    i = total_old_bookings + 1  # used to assign the correct booking ID
    true_or_false = 0  # 0 means false
    new_bookings = [old_bookings[0], old_bookings[1], old_bookings[2]]
    slot1 = old_bookings[0]  # saves the value of old_bookings[0] before it gets deleted and replaced by a new value
    slot2 = old_bookings[1]  # saves the value of old_bookings[1] before it gets deleted and replaced by a new value
    slot3 = old_bookings[2]  # saves the value of old_bookings[2] before it gets deleted and replaced by a new value
    extra, total_bookings = read_extras("extras.txt")
    print()
    print("LONG ISLAND HOLIDAYS - Making a Booking")
    print("=======================================")
    print()
    surname = validating_user_inputs.read_letters_and_apostrophes_only("Enter your family name ==> ").capitalize()
    while len(str(surname)) > 14:
        print("The Family Name cannot be longer than 14 characters. ")
        surname = validating_user_inputs.read_letters_and_apostrophes_only("Enter your family name ==> ").capitalize()
    mobile = validating_user_inputs.read_positive_integer("Enter your phone number ==> ")
    while len(str(mobile)) > 11:
        print("The telephone number cannot be longer than 11 digits. ")
        mobile = validating_user_inputs.read_positive_integer("Enter your phone number ==> ")
    print("Choose your accommodation type:")
    print()
    print(f"1. Deluxe Caravan (€{price[0]}) {old_bookings[0]} Booked")
    print(f"2. Standard Caravan (€{price[1]}) {old_bookings[1]} Booked")
    print(f"3. Camp Site (€{price[2]}) {old_bookings[2]} Booked")
    print("4. No Booking")
    print()
    choice = int(input("Please choose one of the above options ===> "))
    while choice > 4 or choice < 1:
        try:
            choice = int(input("Please choose one of the above options ===> "))
        except ValueError:
            print("Please choose between option 1, option 2 & option 3 by typing the desired options number. ")
    if choice == 1:
        accommodation = "Deluxe Caravan"
        accommodation_cost = price[0]
        total_people = int(input("How many people in your group? "))
        new_bookings.pop(0)
        new_bookings.insert(0, slot1 + 1)  # inserts the value old_bookings[0] + 1 at [0] in the list
    elif choice == 2:
        accommodation = "Standard Caravan"
        accommodation_cost = price[1]
        total_people = int(input("How many people in your group? "))
        new_bookings.pop(1)
        new_bookings.insert(1, slot2 + 1)  # inserts the value old_bookings[1] + 1 at [1] in the list
    elif choice == 3:
        accommodation = "Camp Site"
        accommodation_cost = price[2]
        total_people = int(input("How many people in your group? "))
        new_bookings.pop(2)
        new_bookings.insert(2, slot3 + 1)  # inserts the value old_bookings[2] + 1 at [2] in the list
    else:
        print()
        accommodation_cost = 0
        total_people = 0
    if choice == 3 or choice == 2 or choice == 1:
        if total_old_bookings < BOOKING_LIMIT:
            pool_pass, current_kids_camp, current_pool_pass = save_extras(total_bookings[0], total_bookings[1],
                                                                          total_people, "extras.txt")
            total_kids_cost = current_kids_camp * KIDS_COST
            total_pool_cost = current_pool_pass * POOL_COST
            total_cost = total_kids_cost + total_pool_cost + accommodation_cost
            print()
            print(f"Booking Details")
            print(f"---------------")
            print(f"Booking ID: {i:02d}")
            print(f"Accommodation Type: {accommodation}")
            print(f"No of People: {total_people}")
            print(f"Pool Pass: {pool_pass}")
            print(f"No. for Kids Club: {current_kids_camp}")
            print(f"Cost €{total_cost}")
            print()
            with open(f"{surname}_{i:02d}.txt", "w") as connection:
                print(f"Booking ID: {i:02d}", file=connection)
                print(f"Accommodation Type: {accommodation}", file=connection)
                print(f"No of People: {total_people}", file=connection)
                print(f"Pool Pass: {pool_pass}", file=connection)
                print(f"No. for Kids Club: {current_kids_camp}", file=connection)
                print(f"Cost €{total_cost}", file=connection)
                true_or_false = 1  # 1 means true

    return new_bookings, true_or_false


def bookings_review():
    print()
    accommodation, price, old_bookings, total_old_bookings = read_bookings_file("bookings_2022.txt")
    number_of_lines_in_bookings = len(accommodation)
    i = 0
    popular_accommodation = ""
    most_booked = -1
    expected_booking_income = 0
    while i < number_of_lines_in_bookings:
        expected_booking_income += price[i] * old_bookings[i]
        print(f"{accommodation[i]}: {old_bookings[i]} Booked")
        if total_old_bookings >= 5:
            if old_bookings[i] > most_booked:
                most_booked = old_bookings[i]
                popular_accommodation = accommodation[i]
        i += 1
    extra, bookings = read_extras("extras.txt")
    number_of_lines_in_extras = len(extra)
    print(f"Total no. of Pool Passes: {bookings[1]}")
    print(f"Total no. for Kids Club: {bookings[0]}")
    expected_extras_booked = []
    i2 = 0
    while i2 < number_of_lines_in_extras:
        expected_extras_booked.append(bookings[i2])
        i2 += 1
    expected_kids_extras_income = expected_extras_booked[0] * KIDS_COST
    expected_pool_extras_income = expected_extras_booked[1] * POOL_COST
    expected_extras_income = expected_kids_extras_income + expected_pool_extras_income
    expected_total_income = expected_booking_income + expected_extras_income
    average_income = expected_total_income / total_old_bookings
    if total_old_bookings >= 5:
        print(f"Most Popular Accommodation: {popular_accommodation}")
    print(f"Expected Income: €{expected_total_income}")
    print(f"Average per booking: €{average_income:.2f}")
    total_sites_left = BOOKING_LIMIT - total_old_bookings
    print(f"Number of remaining sites: {total_sites_left}")
    print()


def main():
    accommodation, price, old_bookings, total_old_bookings = read_bookings_file("bookings_2022.txt")
    new_bookings = old_bookings
    ch = menu()
    while ch != 3:
        if ch == 1:
            if sum(new_bookings) < BOOKING_LIMIT:
                new_bookings, true_or_false = booking()
                if true_or_false == 1:
                    update_bookings_file("bookings_2022.txt", accommodation, price, new_bookings)
            else:
                print(
                    f"The booking cannot be created because the booking limit of {BOOKING_LIMIT} bookings has "
                    f"been reached.")
                print()
        elif ch == 2:
            accommodation, price, old_bookings, total_old_bookings = read_bookings_file("bookings_2022.txt")
            if total_old_bookings < 1:
                print()
                print(f"Cannot review bookings because none have been made yet. ")
                print()
            else:
                bookings_review()
        ch = menu()


if __name__ == '__main__':
    main()
