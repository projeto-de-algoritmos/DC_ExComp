def convert_to_digits(string):
    # Convert the string to uppercase
    string = string.upper()

    # Initialize an empty result string
    result = ""

    # Divide and conquer function:
    def divide_and_conquer(string):
        # Base case: if the string is empty or has only one character, return it
        if len(string) <= 1:
            return string

        # Calculate the middle index of the string
        mid = len(string) // 2

        # Divide the string into two substrings: the first half and the second half
        left = string[:mid]
        right = string[mid:]

        # Recursively apply the divide and conquer approach to each of the two substrings
        left = divide_and_conquer(left)
        right = divide_and_conquer(right)

        # Combine the results and return them
        return left + right

    # Divide and conquer the input string
    string = divide_and_conquer(string)

    # Iterate through each character in the divided and conquered string
    for char in string:
        # If the character is a digit, add it to the result string
        if char.isdigit():
            result += char
        # If the character is a letter, convert it to a digit
        elif char.isalpha():
            # Map letters in the 1-3 group to the corresponding digits
            if char in "ABC":
                result += "2"
            elif char in "DEF":
                result += "3"
            elif char in "GHI":
                result += "4"
            elif char in "JKL":
                result += "5"
            elif char in "MNO":
                result += "6"
            # Map letters in the 4-6 group to the corresponding digits
            elif char in "PQRS":
                result += "7"
            elif char in "TUV":
                result += "8"
            elif char in "WXYZ":
                result += "9"
        # If the character is a '*' or '#', add it to the result string
        elif char in "*#":
            result += char

    return result

#input until EOF
while True:
    try:
        input_string = input()
        output_string = convert_to_digits(input_string)
        print(output_string)
    except EOFError:
        break
  