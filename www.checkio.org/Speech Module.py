#Stephen got his speech module broken. This module is responsible for the number pronunciation. He had to click all the digits in the number, and when those were big numbers it could take him a long time. Help the robot to write the speech module for him to speak to his friends easier and quicker. All words in string must be separated by exactly one space character.

#Input: Integer number. From 0 to 1000

#Output: String representation of this number

def checkio(number):
    str_1number = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    str_2number = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
    str_3number = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']

#    print number
    
    if number < 10:
        return str_1number[number - 1]

    if number >= 10 and number < 20:
        return str_2number[number % 10]

    if number >= 20 and number < 100:
        if number % 10 == 0:
            return str_3number[(number - (number % 10)) / 10 - 1]
        else:
            return str_3number[(number - (number % 10)) / 10 - 1] + " " + checkio(number % 10)

    if number >= 100 and number < 1000:
        return str_1number[(number - (number % 100)) / 100 - 1] + " hundred " + checkio(number % 100)
        
#    return 'string representation of n'

if __name__ == '__main__':
    assert checkio(4) == 'four', "First"
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12)=='twelve', "Third"
    assert checkio(101)=='one hundred one', "Fifth"
    assert checkio(212)=='two hundred twelve', "Sixth"
    assert checkio(40)=='forty', "Seventh, forty - it is correct"

    print 'All ok'