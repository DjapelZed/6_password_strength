import re


#WEIGHTS
PASSWORD_LENGTH_WEIGHT = {'max' : 3, 'medium' : 2, 'min' : 1}
PASSWORD_CASE_WEIGHT = {'max': 2, 'min' : 0}
PASSWORD_NUMS_WEIGHT = {'max' : 2, 'medium' : 1, 'min' : 0}
PASSWORD_CHARS_WEIGTH = {'max' : 2, 'medium' : 1, 'min' : 0}
PASSWORD_BLACKLIST_WEIGHT = {'max' : 1, 'min' : 0}


def get_password_length(password):
    if len(password) >= 10:
        return PASSWORD_LENGTH_WEIGHT['max']
    elif len(password) >= 8:
        return PASSWORD_LENGTH_WEIGHT['medium']
    elif len(password) >= 6:
        return PASSWORD_LENGTH_WEIGHT['min']
    return 0


def get_password_case(password):
    if password != password.lower() and password != password.upper():
        return PASSWORD_CASE_WEIGHT['max']
    else:
        return PASSWORD_CASE_WEIGHT['min']


def get_password_nums(password):
    password_nums = re.findall(r'\d', password)
    if len(password_nums) > 4:
        return PASSWORD_NUMS_WEIGHT['max']
    elif len(password_nums) > 2:
        return PASSWORD_NUMS_WEIGHT['medium']
    else:
        return PASSWORD_NUMS_WEIGHT['min']


def get_password_chars(password):
    password_chars = len(re.findall(r'\W', password))
    if password_chars >= 2:
        return PASSWORD_CHARS_WEIGTH['max']
    elif password_chars >= 1:
        return PASSWORD_CHARS_WEIGTH['medium']
    else:
        return PASSWORD_CHARS_WEIGTH['min']


def load_data(filepath):
    with open(filepath) as blacklist:
        blacklist = blacklist.read().splitlines()
    return blacklist


def compare_with_blacklist(data, password):
    if password not in data:
        return PASSWORD_BLACKLIST_WEIGHT['max']
    else:
        return PASSWORD_BLACKLIST_WEIGHT['min']


def get_password_strength(password, filepath):
    password_strength = get_password_length(password) + get_password_case(password) + \
                        get_password_chars(password) + get_password_nums(password) + \
                        compare_with_blacklist(load_data(filepath), password)
    return password_strength


if __name__ == '__main__':
    user_password = input('Password: ')
    filepath = input('File path: ')
    print('Password rating:', get_password_strength(user_password, filepath))
