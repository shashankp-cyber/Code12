def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def get_int_input(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Please enter a value.")
            continue
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid whole number.")


def main():
    print("Hello, GitHub!")

    name = get_non_empty_input("Enter your name: ")
    print(f"Welcome, {name}!")

    age = get_int_input("How old are you? ")
    print(f"Nice to meet you, {name}. You are {age} years old.")

    print("\nHere's a fun brown bear fact:")
    print("The brown bear (Ursus arctos) is native to northern Eurasia and North America.")
    print("Some brown bears can grow up to 9 feet tall when standing on their hind legs.")


if __name__ == "__main__":
    main()
