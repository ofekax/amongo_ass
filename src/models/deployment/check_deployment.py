def is_one_digit_user(username: str) -> bool:
    count: int = 0
    for char in username:
        if char.isdigit():
            count += 1
    return count == 1


def add_0_to_one_digit_username(username: str) -> None:
    fix_username: str = ''
    for char in username:
        if not char.isdigit():
            fix_username = fix_username + char
        else:
            fix_username = fix_username + '0' + char

    print(fix_username)
