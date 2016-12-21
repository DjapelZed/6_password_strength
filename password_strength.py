import re


def get_password_length(password):
    if len(password) > 6 and len(password) < 8:
        return 1
    elif len(password) >= 8 and len(password) < 10:
        return 2
    elif len(password) >= 10:
        return 3
    else:
        return 0

def get_password_case(password):
    if password != password.lower() and password != password.upper():
        return 2
    else:
        return 0


def get_password_nums(password):
    password_nums = re.findall(r'\d', password)
    password_date = re.findall(r'\d{2}\d{2}\d{4}', password)
    if len(password_nums) > 4 and password_nums != password_date:
        return 2
    elif len(password_nums) > 4 and password_nums == password_date:
        return 1
    else:
        return 0

def get_password_chars(passsword):
    passsword_chars = len(re.findall(r'\W', passsword))
    if passsword_chars >= 1 and passsword_chars <= 2:
        return 1
    elif passsword_chars > 2:
        return 2
    else:
        return 0

def load_data(filepath):
    with open(filepath) as blacklist:
        blacklist = blacklist.read().splitlines()
    return blacklist


def compare_with_blacklist(data, password):
    if password not in data:
        return 1
    else:
        return 0


def get_password_strength(password, filepath):
    password_strength = get_password_length(password) + get_password_case(password) + \
                        get_password_chars(password) + get_password_nums(password) + \
                        compare_with_blacklist(load_data(filepath), password)
    return password_strength

if __name__ == '__main__':
    user_password = input('Password: ')
    filepath = input('File path: ')
    print('Password rating:',get_password_strength(user_password, filepath))