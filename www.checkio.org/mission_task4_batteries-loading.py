import random
import itertools

def checkio(stones):
    '''
    minimal possible weight difference between stone piles
    '''
    l = len(stones)
    
    min_weight = 0


    

    for i in range(l):
        min_weight += stones[i]

#    print "min_weight", min_weight

    iter = itertools.permutations(stones)

    mystones = list(iter)
    ll = len(mystones)
    
    for j in range(ll):
        stones = mystones[j]
        
        for i in range(l + 1):
#            print "i=", i
            lefthand = stones[0 : i]
            righthand = stones[i:]
#            print lefthand
#            print righthand
            lefthand_weight = 0
            righthand_weight = 0

            for m in range(len(lefthand)):
                lefthand_weight += lefthand[m]

            for n in range(len(righthand)):
                righthand_weight += righthand[n]

            diff_weight = abs(lefthand_weight - righthand_weight)
#            print "diff_weight=", diff_weight
        
            if diff_weight < min_weight:
                min_weight = diff_weight

    return min_weight
        
if __name__ == '__main__':
    assert checkio([10,10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5,5,6,5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    print 'All is ok'