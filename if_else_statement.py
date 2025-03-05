# Iver John R Monroy
# ITELEC2
# Laboratory # 09 - Guided Coding Exercise: if...else Statement in Python

def main():
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        if number % 2 == 0:
            print("The number", number, "is Even.")
        else:
            print("The number", number, "is Odd.")

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()