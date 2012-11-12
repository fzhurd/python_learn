# Help Nikola write a password security check module for Sofia. Password is considered to be strong enough if its length is more than or equal 10 symbols and it has at least one digit, one upper and one lower case letters.
# Input data: String which is a password.
# Output data: True if the password is safe.


def checkio(data):
    'Return True if password strong and False if not'
    
    isGreatThan10Symbols = False
    
    if len(data) >= 10:
        isGreatThan10Symbols = True

        
    isDigit = False
    isUpper = False
    isLower = False

    l = len(data)
    for i in range(l):
        if data[i].isdigit():
            isDigit = True
            break

    for i in range(l):
        if data[i].isupper():
            isUpper = True
            break

    for i in range(l):
        if data[i].islower():
            isLower = True
            break

    if isGreatThan10Symbols and isDigit and isUpper and isLower:
        return True
    else:
        return False
    
    

if __name__ == '__main__':
    assert checkio('A1213pokl')==False, 'First'
    assert checkio('bAse730onE4')==True, 'Second'
    assert checkio('asasasasasasasaas')==False, 'Third'
    assert checkio('QWERTYqwerty')==False, 'Fourth'
    assert checkio('123456123456')==False, 'Fifth'
    assert checkio('QwErTy911poqqqq')==True, 'Sixth'
    print 'All ok'