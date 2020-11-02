#import pytest --> nie chce mi zaipmortować modułu pytest mimo że jest zainstalowany

def is_palindrome(palindrome: str) -> bool:
    """
    Function to check a string is palindrome.
    :param palindrome: string
    :return: True/False
    """
    s = ''.join(c for c in palindrome if c.isalnum()).lower()
#   rev = ''.join(reversed(palindrome))
    if s == s[::-1]:
        return True
    return False


def test_is_palindrome():
    tester = 'Kobyła ma mały bok!'

    result = is_palindrome(tester)

    assert result is True


#def test_raises_exception_on_non_string_arguments():
#    with pytest.raises(TypeError):
#        is_palindrome(1)


a = input('Enter text you want to check:')

if is_palindrome(a):
    print('{} is palindrome'.format(a))
else:
    print('{} is not palindrome'.format(a))
