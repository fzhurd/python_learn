#Write a program that, depending on the Sofia¡¯s and old man¡¯s starting bargaining sums, the step on which they will increase or decrease the price during the argument, will calculate on which price they will agree.

#Input data: contains four integer numbers: the initial Sofia's offer, Sofia's raise to his offer, the initial fare required by the old man, and the old man's reduction of his fare;
#Output data: the amount of money that Sofia will pay for the spaceship.


def checkio(offers):
    """
       the amount of money that Petr will pay for the ride
    """
    initial_petr, raise_petr, initial_driver, reduction_driver = offers
    while   True:
        initial_petr = initial_petr + raise_petr
        initial_driver = initial_driver - reduction_driver
        if initial_petr >= initial_driver:
            return initial_petr

if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, 'First'
    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    print 'All is ok'
    
    