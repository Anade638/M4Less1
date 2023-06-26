str = "лепсспел"
def checker_palindrom(str):
    reversed_str = str[::-1]
    if str == reversed_str:
        return True
        print('True')
    else:
        return False
        print('False')