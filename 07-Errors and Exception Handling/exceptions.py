def ask():
    while True:
        try:
            num = int(input("Please enter a number: "))
        except ValueError:
            print("That's not a valid number. Please try again.")
            continue
        else:
            print(f"Thank you! You entered the number {num}.")
            break
        finally:
            print("Execution of the input operation is complete.")

if __name__ == "__main__":
    ask()