
def input_error(func):
    # Створюємо декоратор для оброблення помилок
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please provide the correct arguments."
        except IndexError:
            return "Incomplete command. Please provide all necessary arguments."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    # Додаємо декоратор input_error та генеруємо вийняток ValueError
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    # Додаємо декоратор input_error та генеруємо вийняток ValueError та KeyError
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    # Додаємо декоратор input_error та генеруємо вийняток ValueError та KeyError
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]

@input_error
def show_all(contacts):
    # Декоратор додано щоб мати один підхід для обробки помилок та на випадок розширення функції
    if not contacts:
        return "No contacts available."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
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
