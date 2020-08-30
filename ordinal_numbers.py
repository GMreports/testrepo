end_range = int(input("Provide end range for list (it automatically starts at 1): "))

numbers = list(range(1, end_range+1))

for number in numbers:

    if number < 11:
        if str(number).endswith('1'):
            print(str(number) + "st.")
        elif str(number).endswith('2'):
            print(str(number) + "nd.")
        elif str(number).endswith('3'):
            print(str(number) + "rd.")
        else:
            print(str(number) + "th.")
    elif (number >= 11) and (number <= 20):
        print(str(number) + "th.")
    else:
        if str(number).endswith('1'):
            print(str(number) + "st.")
        elif str(number).endswith('2'):
            print(str(number) + "nd.")
        elif str(number).endswith('3'):
            print(str(number) + "rd.")
        else:
            print(str(number) + "th.")

input("\nDone...")