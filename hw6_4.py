def parse_input(user_input):
    if not user_input.strip():
        cmd = ""
        return cmd, []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    name = name.capitalize()
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command."
    name, phone = args
    name = name.capitalize()
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if not args:
        return "Please enter a name."
    name = args[0]
    name = name.capitalize()
    phone = contacts.get(name)

    if phone:
        return phone
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "Contacts list is empty."
    result = [f"{name} {phone}" for name, phone in contacts.items()]
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
         
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "":
            print("Command is empty. Please try again. ")    
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
