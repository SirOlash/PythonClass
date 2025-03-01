import re

def valid_input():
    while True:
        binary_input = input("Please enter an eight digit binary number: ").strip()
        if re.fullmatch(r"[01]{8}", binary_input):
            return binary_input
        else:
            print("Please enter a valid binary number: ")

def main():
    while True:
        user_input = valid_input()
        on_off = user_input[7]
        if on_off == '0':
            print("Display is off")
            choice = input("Do you want to continue? -1 to exit: ")
        else:
            top = " #### " if user_input[0] == '1' else "      "
            middle = " #### " if user_input[6] == '1' else "      "
            bottom = " #### " if user_input[3] == '1' else "      "
            left_upper = "#" if user_input[5] == '1' else "  "
            right_upper = "#" if user_input[1] == '1' else "  "
            upper_row = left_upper + "    " + right_upper
            left_lower = "#" if user_input[4] == '1' else "  "
            right_lower = "#" if user_input[2] == '1' else "  "
            lower_row = left_lower + "    " + right_lower

            print(top)
            print(upper_row)
            print(upper_row)
            print(upper_row)
            print(middle)
            print(lower_row)
            print(lower_row)
            print(lower_row)
            print(bottom)
            choice = input("Do you want to continue? -1 to exit: ")

        if choice == '-1':
            break

if __name__ == "__main__":
    main()
