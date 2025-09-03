# A simple calculator that runs until the user types 'exit'

while True:
    user_input = input("Enter a math expression (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        result = eval(user_input)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}. Please enter a valid expression.")
