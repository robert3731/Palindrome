def is_palindrome(palindrome):
    '''
    Function to check if argument is palindrome.
    Argument must be string.
    '''

    if type(palindrome) == str:
        s = ''.join(c for c in palindrome if c.isalnum()).lower()
        rev = ''.join(reversed(s))
        if s == rev:
            return True
    else:
        print('Type if the argument must be str!')        
    return False


a = 'Kobyła ma mały bok!'

if is_palindrome(a):
    print('{} is palindrome'.format(a))
else:
    print('{} is not palindrome'.format(a))