def check_database_name(username: str, db_name: str) -> bool:
    if not db_name.startswith(username):
        print('your database name should start with your username')
        return False
    return True


def username_contains_more_then_3_chars(username: str) -> bool:
    return len(username) > 2


def is_one_digit_user(username: str) -> bool:
    count: int = 0
    for char in username:
        if char.isdigit():
            count += 1
    return count == 1


def fix_username(username: str) -> str:
    new_username: str = ''
    for char in username:
        if not char.isdigit():
            new_username = new_username + char
        else:
            new_username = new_username + '0' + char

    return new_username


def check_username(username: str) -> str:
    if is_one_digit_user:
        return fix_username(username)
    else:
        return username


def is_good_deployment_data(username: str, db_name: str) -> bool:
    return not check_database_name(username, db_name) and username_contains_more_then_3_chars(username)
