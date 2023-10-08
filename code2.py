def get_age():
    # Get age as a string from the user
    age_str = input("Please enter your age: ")
    
    # Check if the input is numeric
    if age_str.isnumeric():
        # Convert the numeric string to an integer
        age = int(age_str)
        
        # Check if the age is greater than or equal to 18
        if age >= 18:
            return age  # Return the valid age
    return None  # Return None for invalid input

def main():
    # Get the age using the get_age function
    age = get_age()
    
    if age:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()
# The change done in this code are in line 6 where the and operator is removed and use of type conversion to convert string datatype to integer to prevent the type error we gwt in the intial code