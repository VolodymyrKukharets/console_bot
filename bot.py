import re

user_dict = {}


def hello_user() -> str:
    return "How can I help you?"


def add_user(name: str, phone_num: str) -> str:
    if validate_phone_number(phone_num):
        user_dict[name] = phone_num
        # print(user_dict)
        return f"User {name} added"
    else:
        return "Invalid phone number. Please enter a valid phone number."


def change_user(name: str, phone_num: str) -> str:
    if name in user_dict:
        if validate_phone_number(phone_num):
            user_dict[name] = phone_num
            return f"Phone number for user {name} was changed"
        else:
            return "Invalid phone number. Please enter a valid phone number."
    else:
        return f"There is no user named {name}"


def phone_user(name: str) -> str:
    if name in user_dict:
        return f"{name}: {user_dict[name]}"
    else:
        return "Contact not found."


def show_all() -> str:
    contacts = []
    for name, phone in user_dict.items():
        contacts.append(f"{name}: {phone}")
    if contacts:
        return "\n".join(contacts)
    else:
        return "No contacts found."


def end_cycle() -> str:
    return "exit"


def input_error(func):
    def inner(*args: str) -> str:
        try:
            result = func(*args)
            return result
        except KeyError:
            return "KeyError: Invalid command. Please try again."
        except ValueError:
            return "ValueError: Invalid command arguments. Please try again."
        except IndexError:
            return "IndexError: Invalid command arguments. Please try again."

    return inner


def validate_phone_number(phone_num: str) -> bool:
    # Validate phone number format
    pattern = r"^\+?\d+$"
    return re.match(pattern, phone_num) is not None


COMMAND_DICT = {
    "hello": hello_user,
    "add": add_user,
    "change": change_user,
    "phone": phone_user,
    "show all": show_all,
    "good bye": end_cycle,
    "close": end_cycle,
    "exit": end_cycle
}

args_for_command = {
    "hello": 0,
    "add": 2,
    "change": 2,
    "phone": 1,
    "show all": 0,
    "good bye": 0,
    "close": 0,
    "exit": 0
}


@input_error
def get_handler(command, *args):
    return COMMAND_DICT[command](*args)


with_arg = ["phone", "change", "add"]
without_arg = ["good bye", "close", "exit", "show all", "hello"]


def main():
    while True:
        user_text = input(">> ").lower().strip()

        user_command = None
        args = []

        for command in with_arg:
            if user_text.startswith(command):
                user_command = command
                args = user_text.replace(command, "").strip().split()
                break

        if user_command is not None:
            if len(args) == args_for_command[user_command]:
                if len(args) == 0:
                    res = get_handler(user_command)
                elif len(args) == 1:
                    res = get_handler(user_command, args[0].capitalize())
                elif len(args) == 2:
                    res = get_handler(user_command, args[0].capitalize(), args[1])
                else:
                    res = "Invalid command arguments. Please try again."
            else:
                res = f"For this command {user_command} you can use only {args_for_command[user_command]} argument(s)"
        elif user_text in without_arg:
            res = get_handler(user_text)
        else:
            res = "Invalid command. Please try again."

        print(res)

        if res == "exit":
            print("Good bye!")
            exit()


if __name__ == "__main__":
    main()
