#!/usr/bin/env python3
# Created By: BrandonBCode
# Date: November, 3rd, 2025
# This program checks if the year given by user is a leap year


def main():

    # get year from user
    user_year = input("Enter a year: ")
    # type cast to integer
    try:
        user_year = int(user_year)

        # check if divisible by 4
        if user_year % 4 == 0:
            # now check if divisible by 100
            if user_year % 100 == 0:
                # check if divisible by 400
                if user_year % 400 == 0:
                    print("{} is a leap year.".format(user_year))
                else:
                    print("{} is not a leap year.".format(user_year))
            else:
                print("{} is a leap year.".format(user_year))
        else:
            print("{} is not a leap year.".format(user_year))
    except ValueError:
        # exception handling
        print("You have to enter a valid year!")
    # end game
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
