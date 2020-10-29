def is_palindrome(palindrome):
    '''
    Function to check if argument is palindrome.
    Argument must be string.
    '''

    if type(palindrome) == str:
        rev = ''.join(reversed(palindrome))
        if palindrome == rev:
            return True
    return False


a = 2

if is_palindrome(a):
    print('{} is palindrome'.format(a))
else:
    print('{} is not palindrome'.format(a))