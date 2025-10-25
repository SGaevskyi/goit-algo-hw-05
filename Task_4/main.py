def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user name"  # для phone
        except KeyError as e:
            return f"Contact {e} not found"  # для phone/change
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added"


@input_error
def change_contact(args: list, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError(name)
    contacts[name] = phone
    return f"Contact {name} changed"


@input_error
def print_phone_numbers(args: list, contacts):
    name = args[0]
    if name not in contacts:
        raise KeyError(name)
    phone = contacts[name]
    return f"Phone number is {phone}"


@input_error
def print_all_contacts(contacts):
    if len(contacts) == 0:
        return "No contacts found"
    result = list()
    for name, phones in contacts.items():
        result.append(f"{name} phone number is {phones}")
    return "\n".join(result)


def main():
    contacts = dict()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["exit", "quit", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(print_phone_numbers(args, contacts))
        elif command == "all":
            print(print_all_contacts(contacts))
        elif command == "help":
            print("Available commands: \n hello \n add 'name' 'phone'\n change 'name' 'phone'\n phone 'name'\n all")
        else:
            print("Invalid command. Enter 'help' for more information.")


if __name__ == "__main__":
    main()
