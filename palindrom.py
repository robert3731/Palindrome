def is_palindrome(palindrome: str) -> bool:
    """
    Function to check a string is palindrome.
    :param palindrome: string
    :return: True/False
    """
# rev = ''.join(reversed(palindrome))
    s = ''.join(c for c in palindrome if c.isalnum()).lower()
    if s == s[::-1]:
        return True
    return False


a = 'Kobyła ma mały bok!'

if is_palindrome(a):
    print('{} is palindrome'.format(a))
else:
    print('{} is not palindrome'.format(a))
