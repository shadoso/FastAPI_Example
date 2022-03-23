from string import ascii_letters, digits, punctuation

ALLOWED = set(ascii_letters + "áÁéÉíÍóÓöçÇ ")
MATCH = 1
MAX_PASSWORD = 16
MIN_LENGTH = 3
MIN_PASSWORD = 9
NAME = 25
SURNAME = 35


def valid_name(name: str, surname: str):
    info = {
        "Name": name.strip().title(),
        "Surname": surname.strip().title()
    }
    info["Fullname"] = info["Name"] + " " + info["Surname"]

    if set(info["Name"]).issubset(ALLOWED) and set(info["Surname"]).issubset(ALLOWED):
        if NAME >= len(info["Name"]) >= MIN_LENGTH <= len(info["Surname"]) <= SURNAME:
            return info, "Successful"

        else:
            return False, "Name length must be between 3 and 25 and Surname between 3 and 35"

    else:
        return False, "Name must contain only letters"


def valid_pass(password: str):
    test = [set(ascii_letters), set(digits), set(punctuation)]

    if " " in password:
        return False, "Password can't contain space"

    if len(password) < MIN_PASSWORD or len(password) > MAX_PASSWORD:
        return False, "Password must be bigger than 8 digits and smaller than 17"

    for loop in test:
        if len(set(password) & loop) < MATCH:
            return False, f"Password isn't safe, it must contain letters, numbers and special characters"

        else:
            return True, "Successful"
