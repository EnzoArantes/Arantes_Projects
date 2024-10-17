import random

# Function to generate a random 4-digit number with no repeating digits
def get_random():
    random_num = ""  # Initialize an empty string for the random number
    random_hold = ""  # Temporary storage for each random digit
    while len(random_num) < 4:
        random_hold = str(random.randint(1, 9))  # Generate a random digit between 1 and 9
        if random_hold not in random_num:  # Ensure no repeated digits
            random_num += random_hold  # Add the digit to the final number
    return random_num

# Get the user's guess for a 4-digit number with no repeats
user_guess = str(input("Enter a 4-digit number with no repeats: "))
random_digits = get_random()  # Generate the random number

# Start the game loop
while True:
    count = 0  # Initialize position counter for matching digits
    if user_guess == random_digits:
        print("WINNER - The number is", random_digits)  # Winning condition if the guess matches
        break  # Exit the loop if the user wins
    else:
        # Check each digit in the user's guess
        for guess_digit in user_guess:
            if guess_digit in random_digits:
                index = random_digits.find(guess_digit)  # Find index of digit in random number
                print("YES", guess_digit, "is present")
                if index == count:  # Check if the digit is in the correct position
                    print("and in the correct position")
            else:
                print(guess_digit, "not present")  # Digit not found in the random number
            count += 1  # Increment position counter for each guess digit

        print("--------------")
        # Ask for another guess if the previous one was incorrect
        user_guess = str(input("Enter another number: "))
