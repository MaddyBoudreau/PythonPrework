#Question 1

def hello_name(user_name):
    user_name = user_name.upper()
    print(f"Hello {user_name}!")


hello_name(input("Enter your name: "))

#Question 2

def first_odds():
    for x in range(1, 100):
        if x % 2 != 0:
            print(x)


first_odds()

#Question 3

def max_num_in_list(my_list):
    return max(my_list)

#Question 4

def is_leap(year):
    leap = False

    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    elif year % 400 == 0:
        leap = True
    else:
        leap = False
    return leap

#Question 5

def is_consecutive(input_list):
    for index, value in enumerate(input_list[:-1]):
        if value + 1 != input_list[index + 1]:
            return False
        else:
            return True


