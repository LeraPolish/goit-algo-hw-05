def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f'ValueError: {e}'
        except KeyError as e:
            return f"KeyError: {e}"
        except IndexError as e:
            return f"IndexError: {e}"
        
    return inner

@input_error
def parse_input(user_input):    
        user_input = user_input.strip() 
        cmd, *args = user_input.split()
        cmd = cmd.lower()
        return cmd, *args

@input_error
def add_contact(args, contacts):
    print(args)
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError('For change contact u need')
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f'Contact updated.'

@input_error
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "Error. Please, write name."

@input_error
def show_all(contacts):
    return contacts

@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()